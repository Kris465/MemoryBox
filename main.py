"""Точка входа в приложение MemoryBox Archiver."""
from archive_manager import ArchiveManager


def main():
    """Основная функция приложения."""
    archiver = ArchiveManager()
    archiver.archive_all_repos()


if __name__ == "__main__":
    main()