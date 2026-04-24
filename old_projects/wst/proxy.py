# proxy.py
"""ConPTY-прокси для wst — перехват вывода терминала на Windows."""

import sys
import os
import subprocess
import threading
import time
from queue import Queue, Empty

from sound_generator import speak_text, marker_block_start, marker_block_end


def run_command_with_output(command):
    """
    Запускает команду, перехватывает stdout/stderr, озвучивает вывод.
    Работает для НЕинтерактивных команд (ls, git, pytest и т.д.).
    """
    marker_block_start()

    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace',
        )

        # Читаем вывод построчно в реальном времени
        while True:
            line = process.stdout.readline()
            if not line:
                break

            line = line.rstrip('\n')
            if line:
                speak_text(line + '\n', line_pause=True)

        process.wait()
        return_code = process.returncode

    except Exception as e:
        speak_text(f"Error: {str(e)}\n", line_pause=False)
        return_code = 1

    marker_block_end()
    return return_code


class SoundShell:
    """
    Интерактивная звуковая оболочка.
    Запускает команды и озвучивает вывод.
    """

    def __init__(self, prompt=None):
        # Определяем prompt в зависимости от оболочки
        if prompt is None:
            if os.name == 'nt':
                self.prompt = "wsh> "
            else:
                self.prompt = "wsh$ "

    def run(self):
        """Запускает интерактивный цикл."""
        from sound_generator import marker_success, marker_error

        print("=" * 50)
        print(" ЗВУКОВОЙ РЕЖИМ ВКЛЮЧЁН")
        print(" Вводи команды — вывод будет озвучен")
        print(" Введи 'exit' или 'quit' для выхода")
        print("=" * 50)
        speak_text("Звуковой режим включён\n")

        while True:
            try:
                command = input(self.prompt)
            except (EOFError, KeyboardInterrupt):
                print()
                speak_text("Выход\n")
                break

            command = command.strip()

            if not command:
                continue

            if command.lower() in ('exit', 'quit'):
                speak_text("Выход\n")
                break

            return_code = run_command_with_output(command)

            if return_code != 0:
                marker_error()
            else:
                marker_success()
