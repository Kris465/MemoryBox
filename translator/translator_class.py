import os
from loguru import logger
import requests
from dotenv import load_dotenv, find_dotenv, set_key


class Translator:
    def __init__(self):
        self.key = self.get_data("IAM_TOKEN")

    def get_key(self):
        load_dotenv(find_dotenv())
        OAuth_token = os.environ.get('AOuth_token')

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = '{"yandexPassportOauthToken":"OAuth_token"}'.replace(
                                                            'OAuth_token',
                                                            OAuth_token)

        response = requests.post(
            'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            headers=headers,
            data=data)

        json_response = response.json()
        TOKEN = json_response['iamToken']
        set_key(".env", "IAM_TOKEN", TOKEN)
        self.key = TOKEN
        os.environ['IAM_TOKEN'] = TOKEN

    def get_data(self, name: str):
        load_dotenv(find_dotenv())
        return os.environ.get(name)

    def translate(self, text, sourse_language):
        IAM_TOKEN = self.key
        folder_id = self.get_data('folder_id')
        target_language = 'ru'
        texts = text

        body = {
            "sourceLanguageCode": sourse_language,
            "targetLanguageCode": target_language,
            "texts": texts,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

        response = requests.post(
            'https://translate.api.cloud.yandex.net/translate/v2/translate',
            json=body,
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            lst = data['translations']
            translation = lst[0]
            return translation['text']
        else:
            self.get_key()
            logger.info("New IAM_TOKEN is asked and set")
            return
