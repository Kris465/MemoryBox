'''
This module translate text
input: string or list of strings
output string
'''

import os
import requests
from dotenv import load_dotenv, find_dotenv

def yandex_tr(texts):
    load_dotenv(find_dotenv())
    IAM_TOKEN = os.environ.get('IAM_TOKEN')
    folder_id = os.environ.get("folder_id")
    target_language = 'ru'

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
        headers = headers
    )

    print(response.text)
    return response.text
