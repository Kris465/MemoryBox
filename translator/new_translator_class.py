import datetime
import os
from dotenv import find_dotenv, load_dotenv
import requests


class YandexAPI:
    def __init__(self):
        self.api_key = None
        self.api_key_expiration = None

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
        self.api_key = json_response['iamToken']
        self.api_key_expiration = datetime.now() + datetime.timedelta(hours=12)
        # сохранение нового ключа и его время истечения в переменные окружения
        os.environ["YANDEX_API_KEY"] = self.api_key
        os.environ["YANDEX_API_KEY_EXPIRATION"] \
            = self.api_key_expiration.isoformat()

    def translate_text(self, text, lang):
        # проверка времени истечения ключа
        if self.api_key_expiration is None or self.api_key_expiration < datetime.now():
            self.get_key()

        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        params = {"key": self.api_key, "text": text, "lang": lang}
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            return response.json()["text"][0]
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                # обновление ключа в случае ошибки 403 (неверный ключ)
                self.get_key()
                # повторный запрос с новым ключом
                params["key"] = self.api_key
                response = requests.post(url, params=params)
                response.raise_for_status()
                return response.json()["text"][0]
            else:
                raise e

