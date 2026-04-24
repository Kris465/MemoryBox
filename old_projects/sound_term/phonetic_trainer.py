#!/usr/bin/env python3
"""
Phonetic Alphabet Trainer — компактный тренажёр для телефона.
Запуск в Termux/Pydroid3: python phonetic_trainer.py

Зависимости: numpy, sounddevice
Установка: pip install numpy sounddevice
"""

import numpy as np
import sounddevice as sd
import sys
import time

# =============================================================================
# КОНФИГУРАЦИЯ
# =============================================================================

SAMPLE_RATE = 44100
DURATION_SEC = 0.4  # Чуть короче для мобильного использования

# Диапазоны частот
FREQ_RANGE_LETTERS_LOW = 400
FREQ_RANGE_LETTERS_HIGH = 1200
FREQ_RANGE_DIGITS_LOW = 300
FREQ_RANGE_DIGITS_HIGH = 400
FREQ_RANGE_SYMBOLS_LOW = 1500
FREQ_RANGE_SYMBOLS_HIGH = 2000
FREQ_NEWLINE = 2500

# =============================================================================
# АЛФАВИТ
# =============================================================================

ascii_printable = ' ' + ''.join([chr(i) for i in range(33, 127)])
cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

ALPHABET = ascii_printable + cyrillic_upper + cyrillic_lower

# =============================================================================
# ОГИБАЮЩИЕ
# =============================================================================


def envelope_attack(length, sample_rate):
    """Нарастание — для заглавных."""
    t = np.linspace(0, 1, int(length))
    return t


def envelope_decay(length, sample_rate):
    """Затухание — для строчных."""
    t = np.linspace(1, 0, int(length))
    return t


def envelope_flat(length, sample_rate):
    """Плоская — для цифр и символов."""
    return np.ones(int(length))


# =============================================================================
# МАППИНГ ЧАСТОТ
# =============================================================================


def create_frequency_map():
    freq_map = {}
    letter_chars = [c for c in ALPHABET if c.isalpha()]
    digit_chars = [c for c in ALPHABET if c.isdigit()]
    symbol_chars = [c for c in ALPHABET if not c.isalnum()]

    def assign_frequencies(chars, low_freq, high_freq):
        num_chars = len(chars)
        if num_chars == 0:
            return {}
        freq_step = (high_freq - low_freq) / max(num_chars - 1, 1)
        return {char: low_freq + i * freq_step for i, char in enumerate(chars)}

    freq_map.update(assign_frequencies(letter_chars, FREQ_RANGE_LETTERS_LOW, FREQ_RANGE_LETTERS_HIGH))
    freq_map.update(assign_frequencies(digit_chars, FREQ_RANGE_DIGITS_LOW, FREQ_RANGE_DIGITS_HIGH))
    freq_map.update(assign_frequencies(symbol_chars, FREQ_RANGE_SYMBOLS_LOW, FREQ_RANGE_SYMBOLS_HIGH))
    freq_map['\n'] = FREQ_NEWLINE
    freq_map['\r'] = FREQ_NEWLINE
    return freq_map


FREQ_MAP = create_frequency_map()


# =============================================================================
# ГЕНЕРАЦИЯ И ВОСПРОИЗВЕДЕНИЕ ЗВУКА
# =============================================================================


def generate_tone(frequency, duration, envelope_func):
    length = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, length, endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    envelope = envelope_func(length, SAMPLE_RATE)
    min_len = min(len(envelope), len(wave))
    envelope = envelope[:min_len]
    wave = wave[:min_len]
    return wave * envelope


def play_tone(tone_array):
    sd.play(tone_array, samplerate=SAMPLE_RATE)
    sd.wait()


def get_envelope_for_char(char):
    """Определяет огибающую для символа."""
    if char.isalpha():
        if char.isupper() or char in cyrillic_upper:
            return envelope_attack
        else:
            return envelope_decay
    return envelope_flat


def encode_char(char):
    """Генерирует и воспроизводит звук для одного символа."""
    if char not in FREQ_MAP:
        return False

    frequency = FREQ_MAP[char]
    envelope_func = get_envelope_for_char(char)
    tone = generate_tone(frequency, DURATION_SEC, envelope_func)
    play_tone(tone)
    return True


def encode_text(text, delay=0.1):
    """Воспроизводит последовательность символов."""
    for char in text:
        if char in FREQ_MAP:
            encode_char(char)
            if delay > 0:
                time.sleep(delay)


# =============================================================================
# ТРЕНАЖЁР
# =============================================================================


class PhoneticTrainer:
    def __init__(self):
        self.letters_mode = True
        self.digits_mode = True
        self.symbols_mode = True
        self.cyrillic_mode = True
        self.latin_mode = True
        self.delay_between_sounds = 0.1

    def get_training_chars(self):
        """Возвращает список символов для тренировки."""
        chars = []
        for c in ALPHABET:
            include = False

            is_letter = c.isalpha()
            is_digit = c.isdigit()
            is_symbol = not c.isalnum()

            is_cyrillic = c in cyrillic_upper or c in cyrillic_lower
            is_latin = not is_cyrillic and c.isascii()

            if is_letter:
                if is_cyrillic and self.cyrillic_mode:
                    include = True
                elif is_latin and self.latin_mode:
                    include = True
            elif is_digit and self.digits_mode:
                include = True
            elif is_symbol and self.symbols_mode:
                include = True

            if include and c not in ('\n', '\r'):
                chars.append(c)

        return chars

    def play_sound_for_char(self, char):
        """Воспроизводит звук и возвращает подсказку."""
        encode_char(char)

        # Подсказка для проверки
        if char == ' ':
            hint = "пробел"
        elif char == '\n':
            hint = "новая строка"
        else:
            hint = f"'{char}'"
        return hint

    def mode_learn(self):
        """Режим обучения: звук → название."""
        print("\n=== РЕЖИМ ОБУЧЕНИЯ ===")
        print("Слушай звук → смотри символ → запоминай")
        print("Enter — следующий, q — выход\n")

        chars = self.get_training_chars()
        if not chars:
            print("Нет символов для тренировки! Проверь настройки.")
            return

        idx = 0
        while True:
            char = chars[idx % len(chars)]
            hint = self.play_sound_for_char(char)

            print(f"\n{hint}")
            cmd = input("> ").strip().lower()
            if cmd == 'q':
                break
            idx += 1

    def mode_test(self):
        """Режим теста: звук → угадай."""
        print("\n=== РЕЖИМ ТЕСТА ===")
        print("Слушай звук → вводи символ → проверяй")
        print("Enter — проверка, q — выход\n")

        chars = self.get_training_chars()
        if not chars:
            print("Нет символов для тренировки! Проверь настройки.")
            return

        correct = 0
        total = 0

        while True:
            import random
            char = random.choice(chars)
            self.play_sound_for_char(char)

            user_input = input("Твой ответ: ").strip()

            if user_input.lower() == 'q':
                break

            if not user_input:
                print(f"Ответ: {char}")
                continue

            total += 1
            if user_input == char:
                print("✓ Верно!")
                correct += 1
            else:
                print(f"✗ Неверно. Правильно: {char}")

            if total % 10 == 0:
                accuracy = correct / total * 100
                print(f"\n--- Прогресс: {correct}/{total} ({accuracy:.0f}%) ---")

        print(f"\nИтого: {correct}/{total} ({correct/max(total,1)*100:.0f}%)")

    def mode_free(self):
        """Свободная тренировка: быстрый поток звуков."""
        print("\n=== СВОБОДНАЯ ТРЕНИРОВКА ===")
        print("Слушай поток символов")
        print("Enter — показать последние 5, q — выход\n")

        chars = self.get_training_chars()
        if not chars:
            print("Нет символов для тренировки! Проверь настройки.")
            return

        import random
        history = []
        old_delay = self.delay_between_sounds
        self.delay_between_sounds = 0.05  # Быстрее для потока

        try:
            while True:
                char = random.choice(chars)
                self.play_sound_for_char(char)
                history.append(char)
                if len(history) > 5:
                    history.pop(0)

                # Проверяем ввод без блокировки (упрощённо)
                # В Termux можно использовать select, но для простоты — таймаут
                time.sleep(0.1)

        except KeyboardInterrupt:
            pass
        finally:
            self.delay_between_sounds = old_delay

        print(f"\nПоследние символы: {''.join(history)}")

    def settings(self):
        """Настройки тренировки."""
        while True:
            print("\n=== НАСТРОЙКИ ===")
            print(f"1. Буквы: {'✓' if self.letters_mode else '✗'}")
            print(f"2. Цифры: {'✓' if self.digits_mode else '✗'}")
            print(f"3. Символы: {'✓' if self.symbols_mode else '✗'}")
            print(f"4. Кириллица: {'✓' if self.cyrillic_mode else '✗'}")
            print(f"5. Латиница: {'✓' if self.latin_mode else '✗'}")
            print(f"6. Задержка между звуками: {self.delay_between_sounds:.2f}с")
            print("0. Назад")

            cmd = input("Выбор: ").strip()

            if cmd == '1':
                self.letters_mode = not self.letters_mode
            elif cmd == '2':
                self.digits_mode = not self.digits_mode
            elif cmd == '3':
                self.symbols_mode = not self.symbols_mode
            elif cmd == '4':
                self.cyrillic_mode = not self.cyrillic_mode
            elif cmd == '5':
                self.latin_mode = not self.latin_mode
            elif cmd == '6':
                try:
                    val = float(input("Задержка (0.01-1.0): "))
                    self.delay_between_sounds = max(0.01, min(1.0, val))
                except ValueError:
                    pass
            elif cmd == '0':
                break

    def run(self):
        """Главное меню."""
        print("\n" + "=" * 40)
        print("  PHONETIC ALPHABET TRAINER")
        print("  Тренажёр фонетического алфавита")
        print("=" * 40)

        while True:
            print("\n--- МЕНЮ ---")
            print("1. Обучение (звук + символ)")
            print("2. Тест (угадай символ)")
            print("3. Свободная тренировка")
            print("4. Настройки")
            print("5. Выход")

            cmd = input("\nВыбор: ").strip()

            if cmd == '1':
                self.mode_learn()
            elif cmd == '2':
                self.mode_test()
            elif cmd == '3':
                self.mode_free()
            elif cmd == '4':
                self.settings()
            elif cmd == '5':
                print("\nУдачи в тренировке! 73!")
                break
            else:
                print("Неверная команда")


# =============================================================================
# ЗАПУСК
# =============================================================================

if __name__ == "__main__":
    try:
        trainer = PhoneticTrainer()
        trainer.run()
    except KeyboardInterrupt:
        print("\n\nПрервано. Удачи!")
    except Exception as e:
        print(f"\nОшибка: {e}")
        print("\nПроверь установку зависимостей:")
        print("  pip install numpy sounddevice")
        sys.exit(1)
