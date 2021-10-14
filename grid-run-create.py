import argparse
import os
from numpy.random import uniform
from playwright.sync_api import sync_playwright
from loguru import logger
from dataclasses import dataclass

@dataclass
class HPO:
    param: str
    value: str
    combo: int=1  # but combo will still be 1

# https://playwright.dev/python/docs/api/class-page#page-evaluate


# right click and copy selector
list_github_repo_names = "a[class='bp3-menu-item bp3-popover-dismiss']"
list_github_branch_names = "div[class='bp3-text-overflow-ellipsis bp3-fill']"
list_github_script_name = "div[class='repo-files-row-info'] span"
list_hpo_examples = "p[class='flag-value']"

argecho_commit_id = "216e5a9c83254ed93339f73c0a52c3366a152776"

def extract_text_list(page,list_context:str,max_list:int = 100,exit_on_string=None,) -> dict:
  """ extract text from a list and return them in array
    list_context examples
      a[class='bp3-menu-item bp3-popover-dismiss']
      ul[class='bp3-menu']
      p[class='flag-value']
    max_list
      maximum number of list to extract
    return
      a text description need not be unique.  postion array has dups
      {text:[line1,line2]}
  """
  logger.debug(f"extracting text from {list_context}")
  text_list={}
  text_select=None
  for i in range(1,max_list):
    logger.debug(i)
    try:
      text_select = page.text_content(f":nth-match({list_context}, {i})")  
      if text_select in text_list:
        text_list[text_select].append(i)
      else:
        text_list[text_select] = [i]
      logger.debug(text_select,flush=True)
      if exit_on_string == text_select:
        print(f"found {exit_on_string}")
        break
    except:
      break
  return(text_list)

def welcome_page_get(page):
  """ wait for welcome page panes to show up"""
  # check for chart header to show up
  x = page.text_content("div[class='chart-wrapper'] > div[class='chart-header'] > h3")
  logger.debug(f"estimated cost {x}")

  # check for chart header to show up
  x = page.text_content("div[class='runs-table-header'] > div[class='runs-table-header-title'] > h3")
  logger.debug(f"number of runs {x}")

  # check for chart header to show up
  x = page.text_content("div[class='nodes-table-header'] > h3")
  logger.debug(f"active sessions {x}")

def credit_left_get(page) -> float:
  page.wait_for_selector("p[class='credit-remaining-balance'] > span:has-text('.')")
  val = page.text_content("p[class='credit-remaining-balance'] > span")
  val = val.strip('$')
  logger.debug(val)
  
  try:
    val=float(val)
  except:
    val=0.0
  return(val)

def low_credit_warning(page) -> bool:
  page.click('text=×');
  #page.click('.css-199ertr');

def run_name(page,prefix:str = None, suffix:str = None, new_name:str = None) -> str:
  """ retrieve the run name and optionally change the run name """
  test_id = page.text_content(f"input[data-test-id='run-name']")  # wait as eval on selector will stop if not found 

  test_id = page.eval_on_selector('input[data-test-id="run-name"]', "el => el.value")
  logger.debug(f"run name is {test_id}")

  if prefix or suffix or new_name:
    page.click("[data-test-id=\"run-name\"]")
    if prefix: test_id = test_id + "-" + test_id
    if suffix: test_id = test_id + "-" + suffix
    if new_name: test_id = new_name
    # Fill [data-test-id="run-name"]
    page.fill('[data-test-id="run-name"]', test_id);
    # Press Enter
    page.press('[data-test-id="run-name"]', 'Enter');

  return(test_id)

def github_repo(page,repo_name:str):
  """ select github repo """
  #body > div:nth-child(16) > div > div > div > div > div > ul
  # use the cached github place
  logger.debug(f"looking for {repo_name}")
  page.click("[placeholder=\"Search...\"]")

  repo_list=extract_text_list(page,list_github_repo_names,exit_on_string=repo_name)

  logger.debug(f"entering {repo_name}")

  # Click a:has-text("gridai/hello_mnists")
  if repo_name in repo_list:
      logger.debug(f"found {repo_name}")
      page.click(f"a:has-text('{repo_name}')") 
  else:
      # Fill [placeholder="Search..."]
      logger.debug(f"fill {repo_name}")
      page.fill("[placeholder=\"Search...\"]", repo_name)
      # Press Enter
      page.press("[placeholder=\"Search...\"]", "Enter")

def git_branch_name(page,branch_name:str):
    #body > div:nth-child(16) > div > div > div > div > div > ul
    # use the cached github place
    logger.debug(f"looking for {branch_name}")
    page.click("text=maincaret-down")

    # wait for the pop up list (what happens when this is empty)
    branch_list=extract_text_list(page,list_github_branch_names,exit_on_string=branch_name)

    logger.debug(f"entering {branch_name}")

    # Click a:has-text("gridai/hello_mnists")
    if branch_name in branch_list:
        logger.debug(f"found {branch_name}")
        page.click(f"a:has-text('{branch_name}')")

def git_hash_id(page,commit_id:str):
  """ select commit id """
  page.click("[placeholder=\"Search...\"]")
  # Click text=maincaret-down
  page.click("text=maincaret-down")

  # Click text=mainSelect a specific commit Id >> div
  page.click(f"a:has-text('Select a specific commit Id'")

  # Click [placeholder="Please enter a valid commit SHA"]
  page.click('[placeholder="Please enter a valid commit SHA"]');

  page.fill('[placeholder="Please enter a valid commit SHA"]', argecho_commit_id);

def script_name_reset(page):
  """ show the current github page and reset to the script name """
  # Click text=RunRUN NAME .Github filePaste a link to a Github file, repository, or choose fro >> :nth-match(button, 3)
  with page.expect_popup() as popup_info:
      page.click("text=RunRUN NAME .Github filePaste a link to a Github file, repository, or choose fro >> :nth-match(button, 3)")
  page1 = popup_info.value
  # Close page
  page1.close()

  page.click('text=RunRUN NAME .Github filePaste a link to a Github file, repository, or choose fro >> :nth-match(button, 2)');

def script_name_set(page,script_path:str,repo_name:str = None):
  """ show the github page and select the script """
  if not(repo_name):
    logger.debug("figuring out the repo name")
    val = page.text_content('div[class="repo-tree-container-header-title"]')
    repo_name = val.split("/")[-1]
    logger.debug(f"repo name is {repo_name}")

  script_list=extract_text_list(page,list_github_script_name,exit_on_string=script_path)

  # Click text=argecho.py
  page.click(f"text={script_path}")

def spot_instance_set(page):    
    # Click text=BetaUse Spot Instance >> :nth-match(span, 2)
    page.click("text=BetaUse Spot Instance >> :nth-match(span, 2)")
    page.screenshot(path="screenshot5.png", full_page=True)

    # div class estimate-cost-number 
    # span class number
    #body > div:nth-child(14) > div > div.bp3-dialog-container.bp3-overlay-content.bp3-overlay-enter-done > div > div > div > div.sc-gZMcBi.QQNOw > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div.sc-kkGfuU.dzPEYl > div.estimate-cost > div > span
    
    estimate_cost_number = page.text_content("div.estimate-cost>div>span")
    logger.debug(estimate_cost_number)

def hpo_examples_get(page,) -> list:
  """ parse Standard Python syntax (examples) and Additional Grid syntax (examples) """

  page.click("textarea")

  hpo_flag_list = [] # --argument:[parameter,number of possibility]
  vals = page.query_selector_all("div[class='flag-terminal']")
  for y in vals:
    hpo_param = y.query_selector("p > span").text_content()  #key
    hpo_param_value = y.query_selector("button").get_attribute('data-txt') # key "value"
    hpo_value = hpo_param_value[len(hpo_param):].strip()
    logger.debug(f"{hpo_param} {hpo_param_value} {hpo_value}")
    if hpo_value == "0.1 | 1e-2": hpo_value=hpo_value.split()[0] # BUG IN UI: cannot handle |

    noquote = hpo_value.strip('"')  # don't want the quote around expression
    try:
      hpo_value_len = len(eval(noquote))
    except:
      hpo_value_len = 1

    hpo_flag_list.append(HPO(hpo_param,hpo_value,hpo_value_len))

  return(hpo_flag_list)
    
def script_arguments_set(page,hpo_examples:dict, max_arguments:int=10, max_experiments:int=50) -> int:
  """ enter the script arguments copied from examples
    stop adding arguments when one of the conditions are met
      max_arguments
      max_experiments
  """

  # Click textarea
  page.click("textarea")

  hpo_list={}
  hpo_combo=1
  i=0
  k=""
  for v in hpo_examples:
    if v.param in hpo_list: 
      k=f'{v.param}{i}'   # dup, add ordinal position at the end 
    else:
      k=v.param
      
    hpo_list[k]=k + " " + v.value  # there can be a case where value is "", adding extra space at the end
    hpo_combo = hpo_combo * v.combo
    logger.debug(f"{v} resulting in {hpo_combo} adding {hpo_list[k]}")
    i += 1
    if i >= max_arguments: break
    if hpo_combo >= max_experiments: break

  logger.debug(f"expect {hpo_combo} experiments from {hpo_list.values()}")

  page.fill("textarea", " ".join(hpo_list.values()))

  textarea = page.text_content("textarea")  
  logger.debug(textarea) 

  # body > div:nth-child(14) > div > div.bp3-dialog-container.bp3-overlay-content.bp3-overlay-enter-done > div > div > div > div.sc-gZMcBi.QQNOw > # div.simplebar-wrapper > div.simplebar-mask > div > div > div > div.sc-kkGfuU.dzPEYl > div.sc-kEYyzF.gFZtTJ > div
  logger.debug(f"expect {hpo_combo} experiments")
  page.wait_for_selector(f"div.sc-kEYyzF.gFZtTJ:has-text('launch {hpo_combo} experiments')")
  number_of_experiments = page.text_content("div.sc-kEYyzF.gFZtTJ")
  logger.debug(number_of_experiments)

  return(number_of_experiments)

def run(page, args, repo_name=None, branch_name=None,script_name=None):

    if repo_name == None:   repo_name=args.repo_name 
    if branch_name == None : branch_name=args.branch_name
    if script_name == None : script_name=args.script_name

    welcome_page_get(page)

    credit_left = credit_left_get(page)

    # Click [data-test-id="new-button"]
    page.click("[data-test-id=\"new-button\"]")

    ## two way to start the run.  click on run or the + button
    # Click [data-test-id="start-menu-run"] >> text=Run
    # page.click("[data-test-id=\"start-menu-run\"] >> text=Run")

    # Click [data-test-id="start-menu-run"] path
    page.click('[data-test-id="start-menu-run"] path');
 
    if credit_left < 10: 
      logger.debug("making the warning disappear")
      # Click text=At this rate, your credits will run out soon. Buy more credits to keep your jobs
      page.click("text=At this rate, your credits will run out soon. Buy more credits to keep your jobs")

    test_id = run_name(page) 
    page.screenshot(path="screenshot1.png", full_page=True)

    github_repo(page,repo_name)
    page.screenshot(path="screenshot2.png", full_page=True)

    git_branch_name(page,branch_name)
    page.screenshot(path="screenshot3.png", full_page=True)

    script_name_set(page,script_name)
    page.screenshot(path="screenshot4.png", full_page=True)

    spot_instance_set(page)
    page.screenshot(path="screenshot5.png", full_page=True)

    hpo_examples = hpo_examples_get(page)
    page.screenshot(path="screenshot6.png", full_page=True)

    script_arguments_set(page, hpo_examples)
    page.screenshot(path="screenshot7.png", full_page=True)

    # Click [data-test-id="submit-new-run"]
    page.click('[data-test-id="submit-new-run"]')
    page.screenshot(path="screenshot8.png", full_page=True)

    # Wait for job to finish
    page.click(f"text=/.*Successfully started run \"{test_id}\".*/")
    page.screenshot(path="screenshot9.png", full_page=True)
 
    # Close page
    page.close()

    # ---------------------
    context.close()
    #browser.close()

    return(test_id)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grid WebUI QA",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  # playwriter
  parser.add_argument('--headless', default=False, type=bool, help="headless browser")
  # common setup 
  parser.add_argument('--url', type=str, default='https://platform.grid.ai/', help='an integer for the accumulator')
  parser.add_argument('--image_path', type=str, default='./images/', help='images saved')
  parser.add_argument('--storage_state', default=f'auth-google-sangkyulee.json', type=str, help="auth state")
  # run create
  parser.add_argument('--repo_name', default="robert-s-lee/argecho", type=str, help="Repo name")
  parser.add_argument('--branch_name', default="main", type=str, help="Branch name")
  parser.add_argument('--script_name', default="argecho.py", type=str, help="Script name")

  args = parser.parse_args()
  
  with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=args.headless)
    context = browser.new_context(storage_state=args.storage_state)

    # Open new page
    page = context.new_page()
    page.goto(args.url)

    run_name = run(page,args)
    logger.debug(run_name)
    if run_name: print(run_name)