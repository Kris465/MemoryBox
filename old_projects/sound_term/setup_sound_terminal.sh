#!/bin/bash

# setup_sound_terminal.sh
# Скрипт для настройки alias st и est

# Определяем, какую оболочку использует пользователь
SHELL_CONFIG_FILE=""
if [[ "$SHELL" == *"bash"* ]]; then
    SHELL_CONFIG_FILE="$HOME/.bashrc"
elif [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_CONFIG_FILE="$HOME/.zshrc"
else
    echo "Не удалось определить файл конфигурации оболочки (поддерживаются bash и zsh)."
    echo "Пожалуйста, добавьте alias вручную."
    exit 1
fi

echo "Обнаружен файл конфигурации: $SHELL_CONFIG_FILE"

# Проверяем, установлены ли alias ранее
if grep -q "alias st=" "$SHELL_CONFIG_FILE" || grep -q "alias est=" "$SHELL_CONFIG_FILE"; then
    echo "Alias 'st' или 'est' уже найдены в $SHELL_CONFIG_FILE."
    read -p "Перезаписать? (y/N): " -n 1 -r REPLY
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Настройка отменена."
        exit 0
    fi
    # Удаляем старые alias
    sed -i '/^alias st=/d' "$SHELL_CONFIG_FILE"
    sed -i '/^alias est=/d' "$SHELL_CONFIG_FILE"
fi

# Получаем абсолютный путь к директории проекта
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Добавляем alias в файл конфигурации
echo "" >> "$SHELL_CONFIG_FILE"
echo "# Sound Terminal Aliases" >> "$SHELL_CONFIG_FILE"
echo "alias st='python $PROJECT_DIR/main.py'" >> "$SHELL_CONFIG_FILE"
echo "alias est='echo \"Для выхода из озвученного терминала введите 'exit'.\"'" >> "$SHELL_CONFIG_FILE"
echo "" >> "$SHELL_CONFIG_FILE"

echo "Alias 'st' и 'est' успешно добавлены в $SHELL_CONFIG_FILE."
echo "Чтобы изменения вступили в силу, выполните: source $SHELL_CONFIG_FILE"
echo "Или перезапустите терминал."