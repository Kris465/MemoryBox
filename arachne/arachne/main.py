# main.py
from spiders.stepper_spider import StepperSpider
from spiders.collector_spider import CollectorSpider
from scrapy.crawler import CrawlerProcess
from loguru import logger


class UserMenu:
    def __init__(self):
        self.tasks = []

    def show_main_menu(self):
        print("\n🎭 Novel Parser Menu 🎭")
        print("1. Parse")
        print("2. Translate")
        print("3. Save")
        print("4. Exit")
        return input("Choose an option (1-4): ")

    def run(self):
        while True:
            choice = self.show_main_menu()

            if choice == "1":
                self.parse_menu()
            elif choice == "2":
                self.translate_menu()
            elif choice == "3":
                self.save_menu()
            elif choice == "4":
                print("Goodbye! 👋")
                break
            else:
                print("Error: Invalid option. Try again.")

    def parse_menu(self):
        print("\n📖 Parse Mode")
        title = input("Novel title: ").strip()
        if not title:
            return

        print("\n🔧 Select Parser Type:")
        print("1. Stepper (chapter by chapter)")
        print("2. Collector (from table of contents)")
        mod = input("Choose (1-2): ")

        if mod == "1":
            self.run_stepper(title)
        elif mod == "2":
            self.run_collector(title)
        else:
            logger.warning("Unknown parser type")

    def run_stepper(self, title):
        url = input("Enter first chapter URL: ").strip()
        chapter = input("Start chapter number (default: 1): ") or "1"

        process = CrawlerProcess()
        process.crawl(
            StepperSpider,
            title=title,
            url=url,
            chapter=int(chapter))
        process.start()
        logger.success(f"Parsing started for {title}!")

    def run_collector(self, title):
        print("\nEnter URLs (one per line, empty line to finish):")
        urls = []
        while True:
            url = input("> ").strip()
            if not url:
                break
            urls.append(url)

        if urls:
            process = CrawlerProcess()
            process.crawl(
                CollectorSpider,
                title=title,
                urls=urls)
            process.start()
            logger.success(f"Parsing started for {title}!")
        else:
            logger.warning("No URLs provided")

    def translate_menu(self):
        print("\n🌍 Translate Mode")
        title = input("Novel title: ").strip()
        if not title:
            return

        language = input("Language (zh/en): ").strip().lower()
        if language not in ["zh", "en"]:
            logger.warning("Only 'zh' or 'en' supported")
            return

        print("\n🔧 Select chapters to translate:")
        print("1. All chapters")
        print("2. From chapter X")
        print("3. From chapter X to Y")
        config = input("Choose (1-3): ")

        # Здесь будет логика перевода
        logger.info(f"Will translate {title} to {language} (config: {config})")

    def save_menu(self):
        print("\n💾 Save Mode")
        title = input("Novel title: ").strip()
        if not title:
            return

        print("\n🔧 Select save format:")
        print("1. Single file")
        print("2. One file per chapter")
        option = input("Choose (1-2): ")

        # Здесь будет логика сохранения
        logger.info(f"Will save {title} in format {option}")


if __name__ == "__main__":
    menu = UserMenu()
    menu.run()
