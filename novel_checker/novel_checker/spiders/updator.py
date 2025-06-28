import scrapy
import random
import time
from urllib.parse import urlparse


class NovelSpider(scrapy.Spider):
    name = 'novel_spider'

    def start(self):
        with open('urls.txt', 'r') as f:
            urls = f.read().splitlines()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            time.sleep(random.uniform(3, 10))

    def parse(self, response):
        domain = urlparse(response.url).netloc
        selector = self.get_selector_for_domain(domain)
        next_chapter = response.css(selector).get()

        if next_chapter:
            yield {
                'url': response.url,
                'next_chapter': next_chapter,
                'status': True,
                'domain': domain
            }
        else:
            yield {
                'url': response.url,
                'status': False,
                'domain': domain
            }

    def get_selector_for_domain(self, domain):
        selectors = {
            'moonlightnovel.com': 'div.navimedia a:contains("Next")::attr(href)',
            'foxaholic.com': 'button.next-chapter::attr(data-url)',
            'default': 'a.next-chapter::attr(href)'
        }
        return selectors.get(domain, selectors['default'])
