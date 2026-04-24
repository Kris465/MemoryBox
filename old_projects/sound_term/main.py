# main.py
import os
import signal
from tty_wrapper import run_tty_wrapper

def signal_handler(sig, frame):
    """Обработчик сигнала для корректного завершения программы"""
    print('\nВыход из sound_term...')
    os._exit(0)

# Регистрируем обработчик сигнала для Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    run_tty_wrapper()
