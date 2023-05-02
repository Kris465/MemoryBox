import os
import requests
from datetime import datetime
from dotenv import load_dotenv, find_dotenv

from writer_to_json import write

class Translator:

    def __init__(self, text):
        self.__key = self.get_key()
        self.__text = text
        self.__rus = ""


    def get_key(self):
        load_dotenv(find_dotenv())
        OAuth_token = os.environ.get('AOuth_token')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {"yandexPassportOauthToken": OAuth_token}

        response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens',
                                 headers=headers,
                                 data=data,
                                 timeout=3)
        print(response)
        write('key', {str(datetime.now()): str(response)})
        return response

    def translate(self):
        load_dotenv(find_dotenv())
        IAM_TOKEN = os.environ.get('IAM_TOKEN')
        folder_id = os.environ.get('folder_id')
        target_language = 'ru'
        texts = self.__text

        body = {
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                json = body,
                                headers = headers,
                                timeout=300)

        print(response.text)
