import os
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# title = input("title: ")
url = input("url: ")
load_dotenv(find_dotenv())
login = os.environ.get('rulate_login')
password = os.environ.get('rulate_password')

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

driver.implicitly_wait(100)
avatar = driver.find_elements(By.CLASS_NAME, 'main-header-avatar')[0].click()

login_input = driver.find_element(By.NAME, 'login[login]')
password_input = driver.find_element(By.NAME, 'login[pass]')

login_input.send_keys(login)
password_input.send_keys(password)

password_input.send_keys(Keys.ENTER)

avatar = driver.find_element(By.CLASS_NAME, 'icon-plus').click()

chapter_number_input = driver.find_element(By.ID, 'Chapter_title')
chapter_number_input.send_keys('23')  # Ключ из json

first_tick_input = driver.find_element(By.NAME, 'Chapter[has_override]')
second_tick_input = driver.find_elements(By.NAME, 'Chapter[ac_read]')[1]
third_tick_input = driver.find_element(By.ID, 'subscription_')
button = driver.find_element(By.NAME, 'yt0')

driver.execute_script("arguments[0].checked = true;", first_tick_input)
driver.execute_script("arguments[0].checked = true;", second_tick_input)
driver.execute_script("arguments[0].checked = true;", third_tick_input)
driver.execute_script("arguments[0].click();", button)

avatar = driver.find_element(
    By.XPATH,
    '//td[@colspan="3"]/a[text()="импортировать текст"]').click()

original_text = driver.find_element(By.NAME, 'TextSource[text]')
original_text.send_keys('Lin Xiaowan coughed and tasted blood in her mouth.')

drop_menu = driver.find_element(By.NAME, 'TextSource[chopper]')
select = Select(drop_menu)
select.select_by_visible_text('не разбивать вообще, я сделаю это вручную')

next_button = driver.find_element(By.XPATH,
                                  "//button[contains(text(), 'Далее')]")
next_button.click()

avatar = driver.find_element(
    By.XPATH, '//*[@id="form-chop-text"]/div[3]/button[2]').click()
avatar = driver.find_element(
    By.XPATH, '//*[@id="o49659548"]/td[3]/a').click()
rus_text = driver.find_element(By.CLASS_NAME, 'text')
rus_text.send_keys('Сюда вставлен перевод')
avatar = driver.find_element(By.XPATH, '//*[@id="sendTranslate"]').click()

avatar = driver.find_element(
    By.XPATH,
    '//*[@id="Tr"]/tbody/tr[2]/td/div/div[4]/form/div[1]/div[1]/button'
    ).click()
