"""Менеджер миграции истории коммитов репозиториев в архив MemoryBox."""
import os
import subprocess
from urllib.parse import urlparse


class ArchiveManager:
    """Класс для миграции истории коммитов из отдельных репозиториев в архивный репозиторий MemoryBox."""

    def __init__(self, repos_file="repos.txt"):
        """Инициализирует архиватор."""
        self.repos_file = repos_file

    def run_command(self, cmd, description):
        """Выполняет команду с минимальным логированием."""
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Ошибка: {result.stderr}")
            return False
        print(f"{description} выполнено")
        return True

    def cleanup_temp_remotes(self, max_repos=100):
        """Очищает временные remote репозитории от предыдущих запусков."""
        for i in range(1, max_repos + 1):
            cmd = f"git remote remove temp_repo_{i}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Удалён временный remote temp_repo_{i}")
            else:
                # Если remote не существует, выходим из цикла
                error_output = result.stderr.strip()
                if "No such remote" in error_output or "does not exist" in error_output:
                    break

    def get_repo_name(self, url):
        """Извлекает имя репозитория из URL."""
        path = urlparse(url).path.rstrip('/')
        repo_name = path.split('/')[-1]
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        return repo_name

    def get_unique_dir_name(self, base_name):
        """Генерирует уникальное имя папки в old_projects."""
        target_dir = f"old_projects/{base_name}"
        if not os.path.exists(target_dir):
            return base_name

        counter = 1
        while True:
            new_name = f"{base_name}_{counter}"
            new_dir = f"old_projects/{new_name}"
            if not os.path.exists(new_dir):
                return new_name
            counter += 1

    def archive_all_repos(self):
        """Мигрирует историю коммитов всех репозиториев из файла в архивный репозиторий."""
        if not os.path.exists(self.repos_file):
            print("Файл repos.txt не найден")
            return

        # Очищаем временные remote репозитории от предыдущих запусков
        self.cleanup_temp_remotes()

        with open(self.repos_file, 'r') as f:
            repos = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        if not repos:
            print("Нет репозиториев для миграции")
            return

        print(f"Найдено {len(repos)} репозиториев для миграции")

        for i, repo_url in enumerate(repos, 1):
            repo_name = self.get_repo_name(repo_url)
            target_dir = self.get_unique_dir_name(repo_name)

            print(f"\nМиграция репозитория {i}/{len(repos)}: {repo_name}")

            commands = [
                (f"git remote add -f temp_repo_{i} {repo_url}", "Добавление временного remote"),
                (f"git merge -s ours --allow-unrelated-histories --no-commit temp_repo_{i}/main", "Подготовка слияния"),
                (f"git read-tree --prefix=old_projects/{target_dir}/ -u temp_repo_{i}/main", "Копирование истории коммитов"),
                (f"git commit -m \"ARCHIVE: Migrated {repo_name} as subdirectory\"", "Фиксация изменений"),
                (f"git remote remove temp_repo_{i}", "Удаление временного remote")
            ]

            success = True
            for cmd, description in commands:
                if not self.run_command(cmd, description):
                    success = False
                    break

            if success:
                print(f"Репозиторий {repo_name} успешно мигрирован в old_projects/{target_dir}")
            else:
                print(f"Ошибка миграции репозитория {repo_name}")

        print(f"\nМиграция завершена!")
        print("Не забудьте выполнить: git push")
        print("Для добавления новых репозиториев обновите файл repos.txt")