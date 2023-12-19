from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://tl.rulate.ru/')

driver.implicitly_wait(100)
avatar = driver.find_elements(By.CLASS_NAME, 'main-header-avatar')[0].click()
print(*avatar)

# actions = ActionChains(driver)
# actions.move_to_element(avatar).perform()
