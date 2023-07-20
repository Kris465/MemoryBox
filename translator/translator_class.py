import os
import requests
from dotenv import load_dotenv, find_dotenv, set_key


class Translator:

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
        IAM_TOKEN = json_response['iamToken']
        set_key(".env", "IAM_TOKEN", IAM_TOKEN)

    def translate(self, text, sourse_language):
        load_dotenv(find_dotenv())
        IAM_TOKEN = os.environ.get('IAM_TOKEN')
        folder_id = os.environ.get('folder_id')
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
            print(response.text)
            data = response.json()
            lst = data['translations']
            translation = lst[0]
            return translation['text']
        else:
            self.get_key()
            return None
