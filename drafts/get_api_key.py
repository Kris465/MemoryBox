import os
import requests
from dotenv import load_dotenv, find_dotenv

def get_key():
    load_dotenv(find_dotenv())
    OAuth_token = os.environ.get('AOuth_token')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'{"yandexPassportOauthToken":"{OAuth_token}"}'

    response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens',
                             headers=headers,
                             data=data,
                             timeout=3)
    print(response)
