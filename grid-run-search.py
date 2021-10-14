import argparse
import os
from playwright.sync_api import sync_playwright
from loguru import logger
from dataclasses import dataclass

@dataclass
class RUN:
    name: str
    date: str
    q: str
    r: str
    c: str
    s: str
    f: str


run_screen_seq = "1"

print(run_screen_seq)

def save_screen(page,args,fieldname="run-screenshot"):
  run_screen_seq = run_screen_seq + 1
  page.screenshot(path=f"{args.image_path}/{fieldname}{run_screen_seq}.png", full_page=True)

def get_run_info(cols) -> RUN:
  logger.debug(f"number of cols {len(cols)}")
  if (len(cols) == 8):  
    return(RUN(
      cols[1].query_selector(":nth-match(span[class='bp3-popover-target'],1)").text_content(),
      cols[1].query_selector(":nth-match(span[class='bp3-popover-target'],2)").text_content(),
      cols[2].query_selector("div").text_content(),
      cols[3].query_selector("div").text_content(), 
      cols[4].query_selector("div").text_content(), 
      cols[5].query_selector("div").text_content(), 
      cols[6].query_selector("div").text_content())
    )
  else:
    return(None)

def get_count(page) -> str:
  """ return number of runs in the list """
  page.click("text=Runs")

  # wait for panel
  txt = page.text_content("div[class='runs-table-header-title'] > h3 > div")
  logger.debug(f"Runs {txt}")

  panel_list = [] # --argument:[parameter,number of possibility]
  vals = page.query_selector_all("table[data-test-id='small-runs-table'] > tbody > tr")
  logger.debug(len(vals))
  for x in vals:
    try:
      run_name = x.query_selector("span[class='bp3-popover-target']").text_content()  
      logger.debug(run_name)
    except:
      break
  return(txt)  

def run_stop(page,args,name:str):
  """ stop the named run """
  pass

def run_detail(page,args):
  run_desc = page.text_content("div.run-details-description")
  page.fill("div.run-details-description", f"{run_desc} 1")
  save_screen(page,args)

  # remove the detail pop-up page
  page.click(".css-199ertr")
  save_screen(page,args)

def run_search(page,args):

  screen=1
  # Click text=Runs
  page.click("text=Runs")
  save_screen(page,args)

  page.click("div.runs-table-header-actions > div > div > button")
  page.fill("div.runs-table-header-actions > div > div > div > input", args.run_name)
  page.press("div.runs-table-header-actions > div > div > div > input", 'Enter')
  ave_screen(page,args)

  page.wait_for_selector(f"table[data-test-id='small-runs-table'] > tbody > tr:has-text('{args.run_name}')")
  ave_screen(page,args)

  # get the first row
  rows = page.query_selector_all("table[data-test-id='small-runs-table'] > tbody > tr")
  if (len(rows) >= 2): # last row is always empty.  if more than one is found, pick the first one
    row = rows[0] # taking the first row
    cols = row.query_selector_all("td")
    run = get_run_info(cols)
    logger.debug(f"{run}")
    logger.debug(row.text_content())

    # bring up experiments
    page.click(f"text={row.text_content()} >> span") # HACK: sure there is a better way
    page.wait_for_selector(f"div[class='exp-name']:has-text('{run.name}')")
    save_screen(page,args)

    # bring up detail page
    page.click(f"span:has-text('{run.name}')") # HACK: sure there is a better way
    page.wait_for_selector(f"div[class='experiment-detail-header']:has-text('{run.name}')")
    save_screen(page,args)

    run_detail(page, args)
  else:
    logger.debug("run not found")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Grid WebUI QA",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  # playwriter
  parser.add_argument('--headless', default=False, type=bool, help="headless browser")
  # common setup 
  parser.add_argument('--url', type=str, default='https://platform.grid.ai/', help='an integer for the accumulator')
  parser.add_argument('--image_path', type=str, default='./images/', help='images saved')
  parser.add_argument('--storage_state', default=f'auth-google-sangkyulee.json', type=str, help="auth state")
  # run search
  parser.add_argument('--run_name', type=str, default='spicy', help="run name")
  # get arguments
  args = parser.parse_args()

  # logging
  logger.add('logs/logs.log', level='DEBUG')

  with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=args.headless)
    context = browser.new_context(storage_state=args.storage_state)

    # Open new page
    page = context.new_page()
    page.goto(args.url)

    # start the unit test
    x=get_count(page)
    logger.debug(f"Runs {x}")

    run_search(page,args)
