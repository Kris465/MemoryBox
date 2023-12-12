from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()


driver.get('https://tl.rulate.ru/')


avatar = driver.find_elements_by_link_text()
print(*avatar)

# actions = ActionChains(driver)
# actions.move_to_element(avatar).perform()
