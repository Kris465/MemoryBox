import os
import time
import psutil
import tkinter as tk
from tkinter import messagebox
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def load_games(filename):
    with open(filename, 'r') as file:
        games = [line.strip() for line in file if line.strip()]
    return games


def check_game_running(games):
    for game in games:
        for process in psutil.process_iter(['name']):
            process_name = process.info['name'].lower()
            # Проверяем, что название игры является частью полного названия процесса
            if process_name.startswith(game.lower()) or game.lower() in process_name:
                return True, process.info['name']  # Возвращаем полное имя процесса
    return False, None


def notify_user(message):
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    messagebox.showwarning("Уведомление", message)
    root.destroy()


def close_game(game_name):
    for process in psutil.process_iter(['name']):
        if game_name.lower() == process.info['name'].lower():
            process.kill()
            print(f"Приложение '{game_name}' закрыто.")
            break


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
    games_file = 'games.txt'
    games = load_games(games_file)

    game_running = False
    current_game = None
    active_game = 0  # Изначально игра не найдена

    while not game_running:
        game_running, current_game = check_game_running(games)
        if not game_running:
            print("Игра не найдена. Ожидание...")
            active_game = 0  # Игра не найдена
            time.sleep(1)  # Ждем 5 секунд перед следующей проверкой
            set_yandex_music_volume(100)

        else:
            set_yandex_music_volume(10)
            active_game = 1  # Игра найдена
    active_game = 1
    print(f"Игра найдена: '{current_game}'")
    print(f"active_game: {active_game}")


if __name__ == "__main__":
    main()
