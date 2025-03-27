import psutil
import time
import win32gui
import win32process
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

set_vol = 10
# set_vol = int(input("укажите значение того какой должна быть громкость музыки когда открыто приложение с аудио: "))

def get_chrome_url():
    # Получаем список всех процессов
    for proc in psutil.process_iter(['pid', 'name']):
        # Проверяем, является ли процесс Google Chrome
        if proc.info['name'] == 'chrome.exe':
            # Получаем дескриптор окна
            def callback(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    if pid == proc.info['pid']:
                        title = win32gui.GetWindowText(hwnd)
                        if title and ' - Google Chrome' in title:
                            # Убираем часть с " - Google Chrome" для чистого заголовка
                            clean_title = title.replace(' - Google Chrome', '')
                            # print(f"Открытый сайт: {clean_title}")
                            # Проверяем, содержит ли заголовок слово "YouTube"
                            if "YouTube" in clean_title or active_game == 1:
                                set_yandex_music_volume(set_vol)
                            else:
                                set_yandex_music_volume(100)

            win32gui.EnumWindows(callback, None)

def set_yandex_music_volume(volume):
    """Устанавливает громкость Яндекс Музыка."""
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "Яндекс Музыка.exe":
            volume_control = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume_control.SetMasterVolume(volume / 100, None)
            # print(f"Громкость Яндекс Музыка установлена на {volume}%")
            return
    # print("Процесс Яндекс Музыка не найден.")


def main():
    """Основная логика программы."""
    while True:
        get_chrome_url()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
