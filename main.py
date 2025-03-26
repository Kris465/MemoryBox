import subprocess
import time
import os

def clear_screen():
    # Очистка экрана в зависимости от операционной системы
    os.system('cls' if os.name == 'nt' else 'clear')

def get_sound_info():
    # Запускаем SoundVolumeView и получаем информацию о звуке в формате CSV
    process = subprocess.Popen(['svcl.exe', '/scomma', 'output.csv'], stdout=subprocess.PIPE)
    process.wait()  # Ждем завершения процесса

    with open('output.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Пропускаем заголовок
            data = line.strip().split(',')

            if len(data) > 1:
                app_name = data[0]

                # Игнорируем "Яндекс Музыка" и "System Sounds"
                if "Яндекс Музыка" in app_name or "System Sounds" in app_name:
                    continue

                # Ищем значение перед dB
                volume_value = "N/A"  # Значение по умолчанию
                for i, value in enumerate(data):
                    if 'dB' in value:
                        if i > 0:  # Проверяем, что есть предыдущее значение
                            volume_value = data[i - 1].strip()  # Получаем значение громкости
                        break  # Выходим из цикла после нахождения dB

                print(f"Приложение: {app_name}, Громкость: {volume_value}")

def main():
    while True:
        clear_screen()  # Очистка экрана перед выводом
        get_sound_info()
        time.sleep(1)  # Обновление раз в секунду

if __name__ == "__main__":
    main()
