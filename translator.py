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
    
    def translate(self, text):
        pass
