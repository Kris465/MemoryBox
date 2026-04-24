# cli.py
"""CLI для wst — команды wsh и wst."""

import sys
import argparse

from proxy import run_command_with_output
from sound_generator import (
    speak_text,
    marker_block_start,
    marker_block_end,
    marker_success,
    marker_error,
)


def cmd_wsh(args):
    """Запускает команду с озвучкой или интерактивную оболочку."""
    if not args.command:
        # Без аргументов — интерактивная звуковая оболочка
        from proxy import SoundShell
        shell = SoundShell()
        shell.run()
        return 0

    command = ' '.join(args.command)
    return_code = run_command_with_output(command)

    if return_code == 0:
        marker_success()
    else:
        marker_error()

    return return_code


def cmd_speak(args):
    """Озвучивает переданный текст тонами."""
    if not args.text:
        print("Использование: wst speak <текст>")
        return 1

    text = ' '.join(args.text)
    marker_block_start()
    speak_text(text)
    marker_block_end()
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog='wst',
        description='wst — звуковой интерфейс для терминала',
    )

    subparsers = parser.add_subparsers(dest='subcommand', help='Доступные команды')

    # wsh — интерактивная оболочка или команда с озвучкой
    wsh_parser = subparsers.add_parser('wsh', help='Звуковой режим (без аргументов) или запуск команды')
    wsh_parser.add_argument('command', nargs=argparse.REMAINDER, help='Команда (опционально)')
    wsh_parser.set_defaults(func=cmd_wsh)

    # wst speak <текст> — озвучить текст
    speak_parser = subparsers.add_parser('speak', help='Озвучить текст тонами')
    speak_parser.add_argument('text', nargs=argparse.REMAINDER, help='Текст для озвучки')
    speak_parser.set_defaults(func=cmd_speak)

    args = parser.parse_args()

    if not args.subcommand:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
