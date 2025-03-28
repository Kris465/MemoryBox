import psutil
import time
import win32gui
import win32process
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

set_vol = 10  # Уровень громкости для Яндекс Музыка

def get_chrome_url(active_game):
    """Проверяет, открыт ли YouTube в Google Chrome, и регулирует громкость."""
    active_brow = 0
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'chrome.exe':
            def callback(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    if pid == proc.info['pid']:
                        title = win32gui.GetWindowText(hwnd)
                        if title and ' - Google Chrome' in title:
                            clean_title = title.replace(' - Google Chrome', '')
                            if "YouTube" in clean_title or active_game == 1:
                                set_yandex_music_volume(set_vol)
                                active_brow = 1
                            else:
                                set_yandex_music_volume(100)
                                active_brow = 0
                            return active_brow

            win32gui.EnumWindows(callback, None)
    return active_brow

def set_yandex_music_volume(volume):
    """Устанавливает громкость Яндекс Музыка."""
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == "Системные Звуки":
            volume_control = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume_control.SetMasterVolume(volume / 100, None)
            return
    print("Процесс Яндекс Музыка не найден.")

def load_games(filename):
    """Загружает список игр из файла."""
    with open(filename, 'r') as file:
        games = [line.strip() for line in file if line.strip()]
    return games

def check_game_running(games):
    """Проверяет, запущена ли какая-либо игра из списка."""
    blacklist = {
        "locationnotificationwindows.exe",
        "rzdiagnostic",
        "trustedinstaller.exe",
        "searchindexer.exe",
        "searchprotocolhost.exe"
    }
    for game in games:
        for process in psutil.process_iter(['name']):
            process_name = process.info['name'].lower()
            if process_name not in blacklist:
                if process_name.startswith(game.lower()) or game.lower() in process_name:
                    return True, process.info['name']
    return False, None

def gmain(active_brow):
    """Основная логика проверки запущенных игр."""
    games_file = 'games.txt'
    games = load_games(games_file)
    if active_brow == 1:
        while True:
            game_running, current_game = check_game_running(games)
            if not game_running or active_brow == 0:
                active_game = 0
                # time.sleep(1)
                set_yandex_music_volume(100)
            else:
                set_yandex_music_volume(set_vol)
                active_game = 1
            return active_game


def main():
    """Основная логика программы."""
    active_game = 0
    active_brow = 0
    while True:
        active_brow = get_chrome_url(active_game)
        active_game = gmain(active_brow)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
