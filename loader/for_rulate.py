import os
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import nltk


class ForRulate:
    def __init__(self, title, url, project):
        self.title = title
        self.url = url
        self.project = self.saw(project)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)

    def logic(self):
        self.log_in()
        for chapter_number, texts in self.project.items():
            self.driver.get(self.url)
            self.create_chapter(chapter_number)
            self.upload_text(texts)

    def log_in(self):
        load_dotenv(find_dotenv())
        login = os.environ.get('rulate_login')
        password = os.environ.get('rulate_password')
        self.driver.get(self.url)
        avatar = self.driver.find_elements(
            By.CLASS_NAME, 'main-header-avatar')[0].click()
        login_input = self.driver.find_element(By.NAME, 'login[login]')
        password_input = self.driver.find_element(By.NAME, 'login[pass]')
        login_input.send_keys(login)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

    def create_chapter(self, chapter_number):
        avatar = self.driver.find_element(By.CLASS_NAME, 'icon-plus').click()
        chapter_number_input = self.driver.find_element(By.ID, 'Chapter_title')
        chapter_number_input.send_keys(chapter_number)
        first_tick_input = self.driver.find_element(
            By.NAME, 'Chapter[has_override]')
        second_tick_input = self.driver.find_elements(
            By.NAME, 'Chapter[ac_read]')[1]
        third_tick_input = self.driver.find_element(By.ID, 'subscription_')
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
        for key in data:
            for i in range(len(data[key])):
                for sub_key in data[key][i]:
                    if len(data[key][i][sub_key]) > 5000:
                        # разделяем строку на предложения
                        sentences = nltk.sent_tokenize(data[key][i][sub_key])
                        new_list = []
                        current_chapter = {}
                        current_sentence = ""
                        chapter_number = 1
                        for sentence in sentences:
                            if len(current_sentence) + len(sentence) + 2 > 5000:
                                # добавляем текущее предложение в главу
                                # и начинаем новую главу
                                current_chapter[sub_key] = current_sentence
                                new_list.append(current_chapter)
                                current_chapter = {}
                                current_sentence = sentence
                                chapter_number += 1
                            else:
                                # добавляем предложение к текущей главе
                                if current_sentence == "":
                                    current_sentence = sentence
                                else:
                                    current_sentence += ". " + sentence
                        # добавляем последнюю главу в список
                        current_chapter[sub_key] = current_sentence
                        new_list.append(current_chapter)
                        # заменяем исходную главу на список глав
                        data[key][i] = new_list
        return data
