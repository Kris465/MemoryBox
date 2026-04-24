#!/usr/bin/env python3
"""
Генератор данных для живых обоев.
Собирает файлы кода из репозиториев и создаёт data.js
"""
from pathlib import Path
from datetime import datetime

# Конфигурация
REPOS_DIR = r"D:\repos"
OUTPUT_FILE = r"D:\repos\wallpaper\live_wallpaper\data.js"

# Расширения файлов, которые нужно исключить
EXCLUDED_EXTENSIONS = {
    '.md', '.env', '.gitignore', '.gitattributes', '.editorconfig',
    '.pyc', '.pyo', '.pyd', '.db', '.sqlite', '.sqlite3',
    '.log', '.txt', '.rst', '.pdf', '.doc', '.docx',
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.bmp',
    '.pickle', '.pkl', '.pth', '.pt', '.onnx', '.h5',
    '.csv', '.tsv', '.parquet', '.feather',
}

# Директории, которые нужно исключить
EXCLUDED_DIRS = {
    '.git', '.venv', 'venv', '__pycache__', 'node_modules',
    'vendor', 'build', 'dist', 'env', '.env', 'migrations',
    'static', 'media', 'images', 'img', 'assets',
    '.qwen', '.idea', '.vscode', 'coverage', '.pytest_cache',
    'web.archive.org', 'archive', 'backup', 'backups',
}

# Расширения файлов кода
CODE_EXTENSIONS = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.jsx': 'javascript',
    '.tsx': 'typescript',
    '.php': 'php',
    '.java': 'java',
    '.cpp': 'cpp',
    '.cc': 'cpp',
    '.cxx': 'cpp',
    '.c': 'c',
    '.h': 'c',
    '.hpp': 'cpp',
    '.cs': 'csharp',
    '.go': 'go',
    '.rs': 'rust',
    '.rb': 'ruby',
    '.swift': 'swift',
    '.kt': 'kotlin',
    '.scala': 'scala',
    '.r': 'r',
    '.R': 'r',
    '.sql': 'sql',
    '.html': 'markup',
    '.htm': 'markup',
    '.css': 'css',
    '.scss': 'scss',
    '.sass': 'sass',
    '.less': 'less',
    '.sh': 'bash',
    '.bash': 'bash',
    '.ps1': 'powershell',
    '.bat': 'batch',
    '.cmd': 'batch',
    '.json': 'json',
    '.yaml': 'yaml',
    '.yml': 'yaml',
    '.xml': 'markup',
    '.toml': 'toml',
    '.ini': 'ini',
    '.cfg': 'ini',
    '.conf': 'ini',
    '.vue': 'vue',
    '.svelte': 'svelte',
}


def is_valid_file(file_path: Path) -> bool:
    """Проверяет, подходит ли файл для обоев."""
    # Проверяем расширение
    if file_path.suffix.lower() in EXCLUDED_EXTENSIONS:
        return False

    # Проверяем, есть ли файл в директориях исключений
    parts = file_path.parts
    for part in parts:
        if part in EXCLUDED_DIRS:
            return False

    # Проверяем, что это файл кода
    if file_path.suffix.lower() not in CODE_EXTENSIONS:
        return False

    return True


def get_language(file_path: Path) -> str:
    """Определяет язык программирования по расширению."""
    return CODE_EXTENSIONS.get(file_path.suffix.lower(), 'plaintext')


def read_file_content(file_path: Path) -> str:
    """Читает содержимое файла с обработкой ошибок кодировки."""
    encodings = ['utf-8', 'cp1251', 'cp1252', 'latin-1', 'iso-8859-1']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                return content
        except (UnicodeDecodeError, UnicodeError):
            continue

    # Если не получилось прочитать, пробуем с заменой ошибок
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read()
    except Exception:
        return ""


def collect_code_files() -> list[dict]:
    """Собирает все файлы кода из репозиториев."""
    code_files = []
    repos_path = Path(REPOS_DIR)

    print(f"Сканирование директории: {repos_path}")

    for file_path in repos_path.rglob('*'):
        if file_path.is_file() and is_valid_file(file_path):
            # Относительный путь от D:\repos
            rel_path = file_path.relative_to(repos_path)

            # Читаем содержимое
            content = read_file_content(file_path)
            # Пропускаем пустые файлы и слишком большие (>50KB)
            if not content or len(content) > 50000:
                continue

            # Определяем язык
            language = get_language(file_path)

            code_files.append({
                'path': str(rel_path),
                'full_path': str(file_path),
                'language': language,
                'content': content,
                'size': len(content),
                'extension': file_path.suffix.lower()
            })

            print(f"  Найдено: {rel_path} ({language})")

    return code_files


def escape_js_string(s: str) -> str:
    """Экранирует строку для использования в JavaScript."""
    # Заменяем обратные слеши на двойные (для Windows путей)
    s = s.replace('\\', '\\\\')
    # Заменяем обратные кавычки
    s = s.replace('`', '\\`')
    # Заменяем ${ чтобы не было интерполяции
    s = s.replace('${', '\\${')
    # Заменяем специальные символы
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\r')
    s = s.replace('\t', '\\t')
    return s


def generate_data_js(code_files: list[dict]):
    """Генерирует data.js файл с данными."""

    # Сортируем файлы по размеру (предпочитаем файлы среднего размера)
    code_files.sort(key=lambda x: abs(x['size'] - 3000), reverse=False)

    # Берём только 50 файлов для производительности
    code_files = code_files[:50]

    js_content = """// Данные для живых обоев
// Сгенерировано: {timestamp}
// Всего файлов: {file_count}

const CODE_FILES = [
""".format(
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        file_count=len(code_files)
    )

    for i, file_info in enumerate(code_files):
        path_escaped = escape_js_string(file_info['path'])
        content_escaped = escape_js_string(file_info['content'])

        js_content += f"""    {{
        path: `{path_escaped}`,
        language: '{file_info['language']}',
        content: `{content_escaped}`,
        size: {file_info['size']}
    }}"""

        if i < len(code_files) - 1:
            js_content += ','
        js_content += '\n'
    
    js_content += """];

// Экспорт для использования
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { CODE_FILES };
}
"""

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\ndata.js создан: {OUTPUT_FILE}")
    print(f"  Всего файлов: {len(code_files)}")


def main():
    print("=" * 60)
    print("Генератор данных для живых обоев")
    print("=" * 60)

    # Собираем файлы
    code_files = collect_code_files()

    if not code_files:
        print("\nНе найдено файлов кода!")
        return

    # Генерируем data.js
    generate_data_js(code_files)

    print("\nГотово! Теперь откройте index.html в Lively Wallpaper")


if __name__ == '__main__':
    main()
