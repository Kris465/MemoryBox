import json
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ..spiders.stepper import Stepper
from loguru import logger


logger.add("file.log",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
           rotation="3 days",
           backtrace=True, diagnose=True)


class ConfigManager:
    """Класс для управления конфигурацией с логированием"""
    def __init__(self, config_dir: Path):
        self.config_dir = config_dir
        self.main_config = config_dir / "stepper_config.json"
        self.site_templates_dir = config_dir / "site_templates"
        self._ensure_dirs()

    def _ensure_dirs(self) -> None:
        try:
            self.site_templates_dir.mkdir(exist_ok=True, parents=True)
            logger.debug(f"Directories verified at {self.site_templates_dir}")
        except Exception as e:
            logger.error(f"Directory creation failed: {e}")
            raise

    def load_config(self) -> Dict[str, Any]:
        try:
            with open(self.main_config, 'r', encoding='utf-8') as f:
                config = json.load(f)
                logger.debug("Config loaded successfully")
                return config
        except FileNotFoundError:
            logger.warning("Config file not found, creating new")
            return {"sites": {}}
        except Exception as e:
            logger.error(f"Config load error: {e}")
            return {"sites": {}}

    def save_config(self, config: Dict[str, Any]) -> bool:
        try:
            with open(self.main_config, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            logger.success("Config saved successfully")
            return True
        except Exception as e:
            logger.error(f"Config save failed: {e}")
            return False


class SpiderCLI:
    def __init__(self):
        self.config_manager = ConfigManager(Path(__file__).parent.parent / "configs")
        logger.info("CLI initialized")

    def run(self) -> None:
        """Основной цикл приложения с логированием"""
        logger.info("Starting Arachne CLI")
        while True:
            try:
                user_choice = self._show_menu()

                if user_choice == "1":
                    self._handle_parse_novel()
                elif user_choice == "2":
                    self.add_site_template()
                elif user_choice == "3":
                    self.list_sites()
                elif user_choice == "4":
                    logger.info("Exiting application")
                    break

            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                continue

    def _show_menu(self) -> str:
        """Отображение меню с логированием выбора"""
        print("\nOptions:")
        print("1. Parse")
        print("2. Add new site template")
        print("3. List available sites")
        print("4. Exit")

        choice = input("Select option: ").strip()
        logger.debug(f"User selected option: {choice}")
        return choice

    def _handle_parse_novel(self) -> None:
        """Обработка парсинга новеллы с полным логированием"""
        logger.info("Starting novel parsing flow")

        url = input("Enter starting chapter URL: ")
        if not url:
            logger.warning("Empty URL provided")
            return

        chapter_num = input("Enter chapter number (default: 1): ")
        if not chapter_num:
            chapter_num = 1
        logger.debug(f"Starting from chapter: {chapter_num}")

        output_file = input("Output filename (default: novel.json): ").strip() or "novel.json"
        logger.debug(f"Output file: {output_file}")

        site_key = self._detect_site_template(url)
        if not site_key:
            logger.warning(f"No template found for URL: {url}")
            if input("Create template? (y/n): ").lower() == 'y':
                self.add_site_template(url)
            return

        self._run_spider(site_key, url, output_file, chapter_num)

    def _run_spider(self, site_key: str, start_url: str,
                    output_file: str, chapter_num: int = 1) -> None:
        """Запуск паука с детальным логированием"""
        logger.info(f"Starting spider for {site_key}")

        settings = get_project_settings()
        settings.update({
            "FEEDS": {
                output_file: {"format": "json"},
            },
            "LOG_LEVEL": "INFO",
            "DEPTH_LIMIT": 1000
        })

        try:
            process = CrawlerProcess(settings)
            process.crawl(
                Stepper,
                site_key=site_key,
                start_url=start_url,
                chapter_num=chapter_num
            )
            logger.debug("Spider configured, starting process...")
            process.start()
            logger.success("Spider completed successfully")
        except Exception as e:
            logger.error(f"Spider failed: {e}")
            raise

    def _detect_site_template(self, url: str) -> Optional[str]:
        """Определяет подходящий шаблон сайта по URL"""
        if not self.stepper_config.exists():
            logger.warning("Config file not found")
            return None

        try:
            with open(self.main_config, 'r', encoding='utf-8') as f:
                config = json.load(f)
                domain = urlparse(url).netloc.replace("www.", "")

                for site_key in config.keys():
                    if site_key.lower() in domain.lower():
                        logger.debug(
                            f"Matched template: {site_key} for URL: {url}")
                        return site_key

                logger.warning(f"No template found for URL: {url}")
                return None

        except Exception as e:
            logger.error(f"Config load error: {e}")
            return None

    def _update_main_config(self, site_key: str, template: dict) -> None:
        """Обновляет основной конфигурационный файл"""
        try:
            config = {}
            if self.main_config.exists():
                with open(self.main_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)

            config[site_key] = template
            with open(self.main_config, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)

            logger.debug(f"Config updated with template: {site_key}")
        except Exception as e:
            logger.error(f"Config update failed: {e}")
            raise

    def list_sites(self) -> None:
        """Выводит список доступных сайтов"""
        try:
            if not self.main_config.exists():
                logger.warning("No config file found")
                print("No templates available yet.")
                return

            with open(self.main_config, 'r', encoding='utf-8') as f:
                config = json.load(f)

            if not config:
                print("No templates available yet.")
                return

            print("\nAvailable site templates:")
            for i, site_key in enumerate(config.keys(), 1):
                print(f"{i}. {site_key}")

            logger.debug(f"Listed {len(config)} templates")

        except Exception as e:
            logger.error(f"Failed to list sites: {e}")
            print("Error loading templates list")


if __name__ == "__main__":
    cli = SpiderCLI()
    cli.run()
