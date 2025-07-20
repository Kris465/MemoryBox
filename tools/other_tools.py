import re


def get_domain_name(link: str):
    webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1', link)
    return webpage_name
