import os
from dotenv import find_dotenv, load_dotenv
from loguru import logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ForRulate:
    def __init__(self, title, url, project):
        self.title = title
        self.url = url
        # Номера глав, которые нужно залить
        self.chapters = ["24", "30", "31"]
        self.project = self.saw(project)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)
        self.wait = WebDriverWait(self.driver, 10)

    def logic(self):
        self.log_in()
        for chapter_number, texts in self.project.items():
            self.driver.get(self.url)
            self.create_chapter(chapter_number)
            self.upload_text(texts)
            logger.info(f"{chapter_number} is added")

    def log_in(self):
        load_dotenv(find_dotenv())
        login = os.environ.get('rulate_login')
        password = os.environ.get('rulate_password')
        self.driver.get(self.url)
        avatar = self.driver.find_elements(
            By.CLASS_NAME, 'main-header-avatar')[0].click()
        login_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, 'login[login]')))
        password_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, 'login[pass]')))
        login_input.send_keys(login)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

    def create_chapter(self, chapter_number):
        avatar = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'icon-plus'))).click()
        chapter_number_input = self.wait.until(
            EC.presence_of_element_located((By.ID, 'Chapter_title')))
        chapter_number_input.send_keys(chapter_number)

        first_tick_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, 'Chapter[has_override]')))
        second_tick_input = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.NAME, 'Chapter[ac_read]')))[1]
        third_tick_input = self.wait.until(
            EC.presence_of_element_located((By.ID, 'subscription_')))
        button = self.driver.find_element(By.NAME, 'yt0')

        self.driver.execute_script("arguments[0].checked = true;",
                                   first_tick_input)
        self.driver.execute_script("arguments[0].checked = true;",
                                   second_tick_input)
        self.driver.execute_script("arguments[0].checked = true;",
                                   third_tick_input)
        self.driver.execute_script("arguments[0].click();", button)

    def upload_text(self, texts):
        avatar = self.driver.find_element(
            By.XPATH, '//td[@colspan="3"]/a[text()="импортировать текст"]')
        avatar.click()
        original_text = self.driver.find_element(By.NAME, 'TextSource[text]')
        original_text.send_keys(texts[0]['origin'])
        drop_menu = self.driver.find_element(By.NAME, 'TextSource[chopper]')
        select = Select(drop_menu)
        select.select_by_visible_text(
            'не разбивать вообще, я сделаю это вручную')
        next_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Далее')]")
        next_button.click()
        save_button = self.driver.find_element(By.CSS_SELECTOR, 'button.save')
        save_button.click()
        u_element = self.driver.find_element(By.CSS_SELECTOR, "td.u a")
        u_element.click()
        t_element = self.driver.find_element(By.CSS_SELECTOR, "td.t textarea")
        t_element.send_keys(texts[1]['translation'])
        t_element.submit()

    def saw(self, data):
        cutted_dict = {}
        for key, value in data.items():
            if key in self.chapters:
                origin_text = value[0]['origin']
                trans_text = value[1]['translation']
                if len(origin_text) > 5000 or len(trans_text) > 5000:

                    origin_chunks = []
                    trans_chunks = []
                    while len(origin_text) > 5000 or len(trans_text) > 5000:

                        origin_cut = origin_text[:5000].rfind('. ') + 1
                        trans_cut = trans_text[:5000].rfind('. ') + 1

                        origin_chunks.append(origin_text[:origin_cut])
                        trans_chunks.append(trans_text[:trans_cut])

                        origin_text = origin_text[origin_cut:]
                        trans_text = trans_text[trans_cut:]

                    origin_chunks.append(origin_text)
                    trans_chunks.append(trans_text)

                    num_parts = len(origin_chunks)
                    new_keys = [f"Глава {key}.{i + 1}" for i
                                in range(num_parts)]

                    for i, new_key in enumerate(new_keys):
                        cutted_dict[new_key] = [{'origin':
                                                 origin_chunks[i]},
                                                {'translation':
                                                 trans_chunks[i]}]
                else:
                    cutted_dict[key] = value
            else:
                continue
        return cutted_dict
