import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-data-dir=./chromeprofile")
options.add_argument('--disable-extensions')
# options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })  #navigator.webdriver = undefined
# driver.get('https://18.foxaholic.com/novel/the-days-of-tempting-the-bamboo-horse/chapter-1-1/')
driver.get('https://bot.sannysoft.com')
time.sleep(225)
driver.quit()
