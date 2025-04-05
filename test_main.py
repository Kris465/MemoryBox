import psutil
import time
import win32gui
import win32process
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from loguru import logger


SET_VOL = 10
NORMAL_VOL = 85
CHECK_INTERVAL = 0.5
GAMES_FILE = 'games.txt'


class VolumeController:
    """Контроллер громкости Яндекс Музыки"""
    @staticmethod
    def set_volume(volume):
        """Устанавливает громкость Яндекс Музыки"""
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == "YandexMusic.exe":
                volume_control = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume_control.SetMasterVolume(volume / 100, None)
                return True
        logger.warning("Процесс Яндекс Музыка не найден")
        return False


class ProcessMonitor:
    """Мониторинг запущенных процессов"""
    def __init__(self):
        self.blacklist = {
            "locationnotificationwindows.exe",
            "rzdiagnostic",
            "trustedinstaller.exe",
            "searchindexer.exe",
            "searchprotocolhost.exe",
            "monotificationux.exe"
        }

    def is_yandex_music_running(self):
        """Проверяет, запущена ли Яндекс Музыка"""
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == "YandexMusic.exe":
                return True
        return False

    def is_game_running(self, games):
        """Проверяет, запущена ли игра из списка"""
        for game in games:
            for process in psutil.process_iter(['name']):
                process_name = process.info['name'].lower()
                if (process_name not in self.blacklist and
                    (process_name.startswith(game.lower()) or
                     game.lower() in process_name)):
                    return True
        return False

    # def is_game_running(self, games):
    #     """Проверяет, запущена ли игра из списка с выводом отладочной информации"""
    #     false_positives = []

    #     for game in games:
    #         game_lower = game.lower()
    #         for process in psutil.process_iter(['name']):
    #             process_name = process.info['name'].lower()

    #             if process_name in self.blacklist:
    #                 continue

    #             if game_lower in process_name or process_name.startswith(game_lower):
    #                 logger.debug(f"Найден подозрительный процесс: {process_name} (сопоставлен с игрой: {game})")
    #                 false_positives.append(process_name)

    #     if false_positives:
    #         logger.warning(f"Ложные срабатывания игр: {', '.join(set(false_positives))}")
    #         with open('false_positives.txt', 'a') as f:
    #             f.write(f"{time.ctime()}: {', '.join(set(false_positives))}\n")

    #     return len(false_positives) > 0

    def is_youtube_opened(self):
        """Проверяет, открыт ли YouTube в Chrome, с базовой обработкой ошибок"""
        try:
            chrome_processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'chrome.exe':
                    chrome_processes.append(proc.info['pid'])

            def check_window(hwnd, pid):
                try:
                    if not win32gui.IsWindowVisible(hwnd):
                        return False

                    _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
                    if window_pid != pid:
                        return False

                    title = win32gui.GetWindowText(hwnd)
                    if not title:
                        return False

                    return (' - Google Chrome' in title and 
                            ('youtube' in title.lower() or 'ютуб' in title.lower()))
                except:
                    return False

            for pid in chrome_processes:
                try:
                    result = [False]

                    def callback(hwnd, param):
                        if check_window(hwnd, param):
                            result[0] = True
                            return False
                        return True

                    win32gui.EnumWindows(callback, pid)
                    if result[0]:
                        return True

                except Exception as e:
                    logger.debug(f"Ошибка при проверке PID {pid}: {e}")
                    continue

            return False

        except Exception as e:
            logger.error(f"Ошибка в is_youtube_opened: {e}")
            return False


class AppController:
    """Главный контроллер приложения"""
    def __init__(self):
        self.monitor = ProcessMonitor()
        self.games = self.load_games()
        self.last_state = None

    def load_games(self):
        """Загружает список игр из файла"""
        try:
            with open(GAMES_FILE, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            logger.error(f"Файл {GAMES_FILE} не найден")
            return []

    def run(self):
        """Основной цикл с автоматическим возвратом громкости"""
        while True:
            try:
                yandex_running = self.monitor.is_yandex_music_running()
                youtube_opened = self.monitor.is_youtube_opened()
                game_running = self.monitor.is_game_running(self.games)

                current_state = {
                    'yandex': yandex_running,
                    'youtube': youtube_opened,
                    'game': game_running
                }

                if current_state != self.last_state:
                    if not yandex_running:
                        logger.debug("Яндекс Музыка не запущена")
                    elif youtube_opened or game_running:
                        VolumeController.set_volume(SET_VOL)
                        logger.info(f"Тихий режим | YouTube: {youtube_opened} | Игра: {game_running}")
                    else:
                        VolumeController.set_volume(NORMAL_VOL)
                        logger.info("Нормальная громкость: ни YouTube, ни игры не активны")

                    self.last_state = current_state

                time.sleep(CHECK_INTERVAL)

            except Exception as e:
                logger.error(f"Ошибка: {e}")
                time.sleep(1)


if __name__ == "__main__":
    logger.add("app.log",
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
               rotation="1 MB",
               retention="10 days")

    app = AppController()
    app.run()
