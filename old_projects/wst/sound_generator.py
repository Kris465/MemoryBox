# sound_generator.py
"""Генератор звуковых сигналов для wst — тоно-символьная озвучка терминала."""

import numpy as np
import sounddevice as sd
import time

from config import (
    SAMPLE_RATE,
    DURATION_CHAR,
    DURATION_LINE_PAUSE,
    FREQ_RANGE_LETTERS_LOW, FREQ_RANGE_LETTERS_HIGH,
    FREQ_RANGE_DIGITS_LOW, FREQ_RANGE_DIGITS_HIGH,
    FREQ_RANGE_SYMBOLS_LOW, FREQ_RANGE_SYMBOLS_HIGH,
    FREQ_NEWLINE, FREQ_CARRIAGE_RETURN, FREQ_TAB,
    FREQ_MARKER_BLOCK_START, FREQ_MARKER_BLOCK_END,
    FREQ_MARKER_ERROR, FREQ_MARKER_SUCCESS,
)

# --- Определение алфавита ---
# Пробел + ASCII Printable Characters (95 штук)
ascii_printable = ' ' + ''.join([chr(i) for i in range(33, 127)])
# Кириллица
cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Полный алфавит
ALPHABET = ascii_printable + cyrillic_upper + cyrillic_lower


# --- Огибающие ---
def envelope_attack(length, sample_rate):
    """Огибающая для заглавной буквы — нарастание амплитуды."""
    t = np.linspace(0, 1, int(length))
    return t


def envelope_decay(length, sample_rate):
    """Огибающая для строчной буквы — затухание амплитуды."""
    t = np.linspace(1, 0, int(length))
    return t


def envelope_flat(length, sample_rate):
    """Плоская огибающая для цифр, символов и спецсигналов."""
    return np.ones(int(length))


# --- Маппинг символ → частота ---
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

    freq_map.update(assign_frequencies(letter_chars,
                                       FREQ_RANGE_LETTERS_LOW,
                                       FREQ_RANGE_LETTERS_HIGH))
    freq_map.update(assign_frequencies(digit_chars,
                                       FREQ_RANGE_DIGITS_LOW,
                                       FREQ_RANGE_DIGITS_HIGH))
    freq_map.update(assign_frequencies(symbol_chars,
                                       FREQ_RANGE_SYMBOLS_LOW,
                                       FREQ_RANGE_SYMBOLS_HIGH))

    # Спецсимволы
    freq_map['\n'] = FREQ_NEWLINE
    freq_map['\r'] = FREQ_CARRIAGE_RETURN
    freq_map['\t'] = FREQ_TAB

    return freq_map


FREQ_MAP = create_frequency_map()


# --- Генерация тона ---
def generate_tone(frequency, duration, envelope_func):
    """Генерирует аудиосигнал с заданной частотой и огибающей."""
    length = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, length, endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    envelope = envelope_func(length, SAMPLE_RATE)
    min_len = min(len(envelope), len(wave))
    envelope = envelope[:min_len]
    wave = wave[:min_len]
    return wave * envelope


# --- Воспроизведение ---
def play_tone(tone_array):
    """Воспроизводит аудиосигнал и ждёт окончания."""
    sd.play(tone_array, samplerate=SAMPLE_RATE)
    sd.wait()


def play_tone_async(tone_array):
    """Воспроизводит аудиосигнал без ожидания (для будущей очереди)."""
    sd.play(tone_array, samplerate=SAMPLE_RATE)


# --- Кодирование текста в звук ---
def encode_char(char, frequency, envelope_func):
    """Генерирует тон для одного символа."""
    return generate_tone(frequency, DURATION_CHAR, envelope_func)


def speak_text(text, line_pause=True):
    """
    Озвучивает полный текст тонами.
    Без фильтрации — каждый символ, как есть.
    """
    for char in text:
        if char == '\n':
            tone = encode_char(char, FREQ_NEWLINE, envelope_flat)
            play_tone(tone)
            if line_pause:
                # Пауза между строками
                time.sleep(DURATION_LINE_PAUSE)
            continue

        if char == '\r':
            tone = encode_char(char, FREQ_CARRIAGE_RETURN, envelope_flat)
            play_tone(tone)
            continue

        if char == '\t':
            tone = encode_char(char, FREQ_TAB, envelope_flat)
            play_tone(tone)
            continue

        if char not in FREQ_MAP:
            # Пропускаем неизвестные символы (управляющие и т.п.)
            continue

        frequency = FREQ_MAP[char]

        # Определяем огибающую
        if char.isalpha():
            if char.isupper() or char in cyrillic_upper:
                envelope_func = envelope_attack
            else:
                envelope_func = envelope_decay
        else:
            envelope_func = envelope_flat

        tone = encode_char(char, frequency, envelope_func)
        play_tone(tone)


# --- Маркеры событий ---
def play_marker(freq, duration=0.3):
    """Воспроизводит звуковой маркер (ошибка, успех и т.д.)."""
    tone = generate_tone(freq, duration, envelope_flat)
    play_tone(tone)


def marker_block_start():
    """Маркер начала блока вывода."""
    play_marker(FREQ_MARKER_BLOCK_START, 0.2)


def marker_block_end():
    """Маркер конца блока вывода."""
    play_marker(FREQ_MARKER_BLOCK_END, 0.2)


def marker_error():
    """Маркер ошибки — низкий нисходящий тон."""
    tone = generate_tone(FREQ_MARKER_ERROR, 0.4, envelope_decay)
    play_tone(tone)


def marker_success():
    """Маркер успеха — высокий восходящий тон."""
    tone = generate_tone(FREQ_MARKER_SUCCESS, 0.3, envelope_attack)
    play_tone(tone)
