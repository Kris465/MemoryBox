import subprocess
from pathlib import Path


def main():
    novel_name = input("Название новеллы: ").strip()
    start_url = input("Стартовая ссылка: ").strip()
    site_name = input("Имя конфига (например, translatingboredom): ").strip()

    output_dir = Path("novels") / novel_name
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "scrapy", "crawl", "universal_novel_spider",
        "-a", f"site_name={site_name}",
        "-a", f"start_url={start_url}",
        "-o", str(output_dir / "content.json"),
    ]
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
