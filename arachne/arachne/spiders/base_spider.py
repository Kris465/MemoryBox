# spiders/base_spider.py
import re
from pathlib import Path
import json
from loguru import logger
import scrapy


class BaseSpider(scrapy.Spider):
    config_dir = "configs"
    
    def extract_domain(self, url):
        return re.sub(r'^https?://(?:www\.)?([^/]+).*$', r'\1', url.lower())
    
    def load_config(self, spider_type, url):
        domain = self.extract_domain(url)
        config_path = Path(__file__).parent.parent / self.config_dir / spider_type / "sites.json"
        
        with open(config_path, encoding="UTF-8") as f:
            configs = json.load(f)
        
        return configs.get(domain, configs["default"])