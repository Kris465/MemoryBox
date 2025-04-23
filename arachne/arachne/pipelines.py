import json
from pathlib import Path
from urllib.parse import urlparse


class NovelJsonPipeline:
    def __init__(self):
        self.novel_data = {}
        self.output_dir = Path("novels")

    def open_spider(self, spider):
        self.output_dir.mkdir(exist_ok=True)
        spider.logger.info(f"Output directory: {self.output_dir.resolve()}")

    def process_item(self, item, spider):
        chapter_key = str(item['chapter_number'])
        self.novel_data[chapter_key] = item['url'] + "\n"

        if hasattr(spider, 'config') and 'output_template' in spider.config:
            for field in spider.config['output_template'].get('meta_fields', []):
                if field in item:
                    self.novel_data[chapter_key] += f"{field}: {item[field]}\n"

        self.novel_data[chapter_key] += item['content']
        return item

    def close_spider(self, spider):
        if not self.novel_data:
            return

        domain = urlparse(next(iter(self.novel_data.values()))).netloc
        filename = f"{domain.replace('www.', '')}.json"
        output_path = self.output_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.novel_data, f, ensure_ascii=False, indent=2)

        spider.logger.info(f"Saved {len(self.novel_data)} chapters to {output_path}")
