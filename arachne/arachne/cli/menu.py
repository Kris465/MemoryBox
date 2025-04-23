import json
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ..spiders.stepper import Stepper


class SpiderCLI:
    def __init__(self):
        self.config_dir = Path(__file__).parent.parent / "configs"
        self.site_templates_dir = self.config_dir / "site_templates"
        self.main_config = self.config_dir / "stepper_config.json"
        self._ensure_dirs()

    def _ensure_dirs(self):
        self.site_templates_dir.mkdir(exist_ok=True, parents=True)

    def run(self):
        print("Arachne")
        while True:
            print("\nOptions:")
            print("1. Parse a novel")
            print("2. Add new site template")
            print("3. List available sites")
            print("4. Exit")

            choice = input("Select option: ").strip()

            if choice == "1":
                self.parse_novel()
            elif choice == "2":
                self.add_site_template()
            elif choice == "3":
                self.list_sites()
            elif choice == "4":
                break
            else:
                print("Invalid option, try again.")

    def parse_novel(self):
        """Основной метод для запуска парсинга"""
        print("\nNovel Parsing Mode")
        url = input("Enter first chapter URL: ").strip()

        site_key = self._detect_site_template(url)

        if not site_key:
            print("No matching site template found for this URL.")
            if input("Create new template? (y/n): ").lower() == 'y':
                self.add_site_template(url)
            return

        print(f"Using template: {site_key}")

        output_file = input(
            "Output filename (default: novel.json): ").strip() or "novel.json"

        self._run_spider(site_key, url, output_file)
        print(f"\nSuccess! Results saved to {output_file}")

    def _detect_site_template(self, url: str) -> Optional[str]:
        """Определяет подходящий шаблон сайта по URL"""
        with open(self.main_config) as f:
            config = json.load(f)

        for site_key, site_data in config["sites"].items():
            if any(domain in url for domain in site_data["allowed_domains"]):
                return site_key
        return None

    def _run_spider(self, site_key: str, start_url: str, output_file: str):
        """Запускает паука Scrapy"""
        settings = get_project_settings()
        settings.update({
            "FEEDS": {
                output_file: {"format": "json"},
            },
            "LOG_ENABLED": True,
            "LOG_LEVEL": "INFO"
        })

        process = CrawlerProcess(settings)
        process.crawl(Stepper, site_key=site_key, start_urls=[start_url])
        process.start()

    def add_site_template(self, known_url: str = None):
        """Добавляет новый шаблон сайта"""
        print("\nAdding New Site Template")

        site_name = input("Site name (key): ").strip()
        base_url = input("Base URL (e.g. https://example.com): ").strip()
        start_url = known_url or input("Example start URL: ").strip()

        print("\nOpen the site in browser and inspect elements to find:")
        content_sel = input("Chapter content CSS selector: ").strip()
        next_sel = input("Next chapter link CSS selector: ").strip()

        template = {
            "base_url": base_url,
            "chapter_content_selector": content_sel,
            "next_chapter_selector": next_sel,
            "start_urls": [start_url],
            "allowed_domains": [urlparse(base_url).netloc.replace("www.", "")]
        }

        template_path = self.site_templates_dir / f"{site_name}.json"
        with open(template_path, "w") as f:
            json.dump(template, f, indent=2)

        self._update_main_config(site_name, template_path)

        print(f"Template '{site_name}' added successfully!")

    def _update_main_config(self, site_key: str, template_path: Path):
        """Обновляет основной конфигурационный файл"""
        if not self.main_config.exists():
            config = {"sites": {}}
        else:
            with open(self.main_config) as f:
                config = json.load(f)

        with open(template_path) as f:
            template = json.load(f)

        config["sites"][site_key] = template

        with open(self.main_config, "w") as f:
            json.dump(config, f, indent=2)

    def list_sites(self):
        """Выводит список доступных сайтов"""
        if not self.main_config.exists():
            print("No site templates available yet.")
            return

        with open(self.main_config) as f:
            config = json.load(f)

        print("\nAvailable site templates:")
        for i, site_key in enumerate(config["sites"].keys(), 1):
            print(f"{i}. {site_key}")


if __name__ == "__main__":
    cli = SpiderCLI()
    cli.run()
