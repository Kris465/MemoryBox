# tty_wrapper.py
import os
import pty
import select
import sys
import signal
from sound_generator import speak_output, speak_input # Импортируем speak_input

def run_tty_wrapper():
    # PID дочернего процесса (bash) и файловый дескриптор мастера PTY
    pid, fd_master = pty.fork()

    if pid == 0:  # Дочерний процесс (здесь запускается bash)
        # Запускаем bash (или любую другую команду)
        os.execlp('bash', 'bash')

    else:  # Родительский процесс (TTY-обертка)
        # Обработчик сигнала SIGWINCH для изменения размера окна
        # Пока убираем _copy_winsize, так как она может отсутствовать
        def handle_resize(signum, frame):
            # pty._copy_winsize(fd_master) # pylint: disable=protected-access
            pass # Пока не делаем ничего при изменении размера

        signal.signal(signal.SIGWINCH, handle_resize)

        try:
            while True:
                # Ждем данные из PTY (вывод bash) или из stdin (ввод пользователя)
                ready, _, _ = select.select([fd_master, sys.stdin], [], [])

                if fd_master in ready:
                    try:
                        # Читаем данные из PTY (вывод команды)
                        output_data = os.read(fd_master, 1024)
                        if not output_data:
                            break # PTY закрыт
                        # Выводим данные в оригинальный терминал (вашему экрану)
                        os.write(sys.stdout.fileno(), output_data)
                        # Озвучиваем прочитанные данные
                        speak_output(output_data.decode('utf-8', errors='ignore'))

                    except OSError:
                        break # PTY закрыт

                if sys.stdin in ready:
                    # Читаем ввод пользователя
                    input_data = os.read(sys.stdin.fileno(), 1024)
                    if not input_data:
                        break # stdin закрыт (например, Ctrl+D)
                    # Озвучиваем вводимые символы (опционально)
                    for char in input_data.decode('utf-8', errors='ignore'):
                         speak_input(char)
                    # Отправляем ввод в PTY (в bash)
                    os.write(fd_master, input_data)

        finally:
            # Закрываем файловый дескриптор мастера PTY
            os.close(fd_master)
            # Ждем завершения дочернего процесса
            os.waitpid(pid, 0)

if __name__ == "__main__":
    run_tty_wrapper()