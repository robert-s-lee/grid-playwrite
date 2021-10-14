References
[Playwriter Python](https://playwright.dev/python/docs/intro/)

# Setup 

Install Playwrite

```bash
conda create --name playwriter python=3.7
conda activate playwriter

pip install playwright
playwright install
```

# Interactive Test
playwright codegen --browser=ff --target=python --load-storage=auth-google-sangkyulee.json https://platform.grid.ai


playwright codegen --browser=ff --output=run-argecho.py --target=python --load-storage=auth-google-sangkyulee.json https://platform.grid.ai

playwright open --browser=ff --load-storage=auth-google-sangkyulee.json https://platform.grid.ai


python run.py

https://platform.grid.ai


pip install -U pip
pip install robotframework-browser
rfbrowser init
```


## Save the auth cookies

```bash
npx playwright codegen --browser=ff --output=login-google-rslee63921.py --target=python --save-storage=auth-google-rslee63921.json https://platform.grid.ai

npx playwright codegen --browser=ff --output=login-google-sangkyulee.py --target=python --save-storage=auth-google-sangkyulee.json https://platform.grid.ai

npx playwright codegen --browser=ff --output=login-github-robert-s-lee.py --target=python --save-storage=auth-github-robert-s-lee.json https://platform.grid.ai
```