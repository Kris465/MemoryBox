#!/bin/bash

OUTPUT_FILE="wifi_networks.txt"

if [ -f "$OUTPUT_FILE" ]; then
    echo "Файл $OUTPUT_FILE уже существует. Он будет перезаписан."
fi

echo "Сканирование Wi-Fi сетей..." > "$OUTPUT_FILE"
echo "Дата: $(date)" >> "$OUTPUT_FILE"
echo "-----------------------------------" >> "$OUTPUT_FILE"

sudo iwlist wlan0 scan | grep -E 'Cell|ESSID|Encryption|Quality' >> "$OUTPUT_FILE"

echo "Сканирование завершено. Результаты записаны в $OUTPUT_FILE."
