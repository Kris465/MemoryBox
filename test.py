from pywinauto import Application
import time

while True:
    try:
        # Подключение к активному окну Chrome
        app = Application(backend='uia').connect(title_re=".*Chrome.*")
        window = app.window(title_re=".*Chrome.*")

        # Получение URL из адресной строки
        url = window.child_window(auto_id="omnibox-input").get_value()

        # Проверка и вывод результата
        if url.strip():  # Если URL не пустой
            print(f"[{time.strftime('%H:%M:%S')}] Активная вкладка: {url}")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Вкладка закрыта или браузер неактивен")

    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Ошибка: Браузер не найден или неактивен")

    # Задержка на 1 секунду
    time.sleep(1)
