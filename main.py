from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = 'https://www.crimsonnovels.com/searchbook'
driver.get(url)


def slow_scroll(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        
        
slow_scroll(driver)

html_code = driver.page_source

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_code)

input("Нажмите Enter, чтобы закрыть окно...")
driver.quit()
