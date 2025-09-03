import os
import subprocess
import sys
from urllib.parse import urlparse


def run_command(cmd, description, cwd=None):
    """Выполняет команду и логирует"""
    print(f"{description}: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True,
                            text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Ошибка: {result.stderr}")
        return False
    print("Успешно")
    return True


def get_repo_name(url):
    """Извлекает имя репозитория из URL"""
    path = urlparse(url).path.rstrip('/')
    repo_name = path.split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]
    return repo_name


def get_unique_dir_name(base_name, base_path):
    """Генерирует уникальное имя папки"""
    target_path = os.path.join(base_path, base_name)
    if not os.path.exists(target_path):
        return base_name

    counter = 1
    while True:
        new_name = f"{base_name}_{counter}"
        new_path = os.path.join(base_path, new_name)
        if not os.path.exists(new_path):
            return new_name
        counter += 1


def main():
    print("MemoryBox Archiver - Начинаем архивацию репозиториев...")
    print("=" * 60)

    repos_file = "repos.txt"
    if not os.path.exists(repos_file):
        with open(repos_file, 'w', encoding='utf-8') as f:
            f.write("# https://github.com/username/old-project.git\n")
        print("Создан файл repos.txt, 1 ссылка == 1 строка")
        sys.exit(0)

    try:
        with open(repos_file, 'r') as f:
            repos = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        sys.exit(1)

    if not repos:
        print("В файле repos.txt нет репозиториев для обработки")
        print("Добавьте ссылки на репозитории в файл")
        sys.exit(1)

    print(f"Найдено {len(repos)} репозиториев для архивации")

    for i, repo_url in enumerate(repos, 1):
        print(f"\n{'='*50}")
        print(f"Репозиторий {i}/{len(repos)}: {repo_url}")
        print(f"{'='*50}")

        # Получаем имя репозитория
        repo_name = get_repo_name(repo_url)
        target_dir = get_unique_dir_name(repo_name, ".")

        print(f"Будет сохранен в: {target_dir}/")

        # Выполняем команды архивации
        commands = [
            (f"git remote add -f temp_repo_{i} {repo_url}",
             "Добавляем временный remote"),
            (f"git merge -s ours --allow-unrelated-histories --no-commit temp_repo_{i}/main",
             "Подготавливаем merge"),
            (f"git read-tree --prefix={target_dir}/ -u temp_repo_{i}/main",
             "Копируем содержимое"),
            (f"git commit -m \"ARCHIVE: Added {repo_name} as subdirectory\"",
             "Фиксируем архив"),
            (f"git remote remove temp_repo_{i}", "Удаляем временный remote")
        ]

        success = True
        for cmd, description in commands:
            if not run_command(cmd, description):
                print(f"Пропускаем репозиторий из-за ошибки")
                success = False
                break

        if success:
            print(f"Репозиторий {repo_name} успешно архивирован!")

    print(f"\n{'='*60}")
    print("Архивация завершена!")
    print("Не забудьте выполнить: git push")
    print("Для добавления новых репозиториев обновите файл repos.txt")


if __name__ == "__main__":
    main()
