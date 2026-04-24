#!/bin/bash

# install.sh - Скрипт для установки alias'ов для sound_term

# Определяем путь к директории проекта
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Находим файл .bashrc или .zshrc в зависимости от используемого шелла
if [ -n "$ZSH_VERSION" ]; then
    RC_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    RC_FILE="$HOME/.bashrc"
else
    RC_FILE="$HOME/.bashrc"  # По умолчанию используем .bashrc
fi

echo "Добавляем alias'ы в $RC_FILE..."

# Добавляем alias для запуска программы с активацией виртуального окружения
echo "" >> "$RC_FILE"
echo "# Alias'ы для sound_term" >> "$RC_FILE"
echo "st() {" >> "$RC_FILE"
echo "    source $PROJECT_DIR/.venv/bin/activate" >> "$RC_FILE"
echo "    python3 $PROJECT_DIR/main.py" >> "$RC_FILE"
echo "    deactivate" >> "$RC_FILE"
echo "}" >> "$RC_FILE"

echo "Установка завершена!"
echo "Для использования:"
echo "- Откройте новый терминал"
echo "- Введите 'st' для запуска программы"
echo "- Введите 'est' в терминале для выхода из программы"