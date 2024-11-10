#!/bin/bash

upgradable_packages=$(apt list --upgradable 2>/dev/null | awk -F/ '{print $1}' | tail -n +2)

declare -a selected_packages

echo "Доступные для обновления пакеты:"
echo "$upgradable_packages"

echo "Введите названия пакетов, которые вы хотите обновить (через пробел):"
read -a selected_packages

if [ ${#selected_packages[@]} -gt 0 ]; then
    sudo apt update
    sudo apt upgrade -y "${selected_packages[@]}"
else
    echo "Не выбрано ни одного пакета для обновления."
fi