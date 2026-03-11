# sound_generator.py
import numpy as np
import sounddevice as sd
import re # Добавим модуль для работы с регулярными выражениями
from config import SAMPLE_RATE, DURATION_SEC, FREQ_RANGE_LETTERS_LOW, FREQ_RANGE_LETTERS_HIGH, FREQ_RANGE_DIGITS_LOW, FREQ_RANGE_DIGITS_HIGH, FREQ_RANGE_SYMBOLS_LOW, FREQ_RANGE_SYMBOLS_HIGH, FREQ_NEWLINE

# --- Определение алфавита ---
# Пробел + ASCII Printable Characters (95 штук)
ascii_printable = ' ' + ''.join([chr(i) for i in range(33, 127)])
# Кириллица (66 букв + ё/Ё)
cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Полный алфавит
ALPHABET = ascii_printable + cyrillic_upper + cyrillic_lower

# --- Определение огибающих ---
def envelope_attack(length, sample_rate):
    """Огибающая для 'заглавной' буквы - нарастание амплитуды."""
    t = np.linspace(0, 1, int(length))
    return t

def envelope_decay(length, sample_rate):
    """Огибающая для 'строчной' буквы - затухание амплитуды."""
    t = np.linspace(1, 0, int(length))
    return t

def envelope_flat(length, sample_rate):
    """Плоская огибающая для цифр и символов."""
    return np.ones(int(length))

# --- Создание маппинга символ -> частота ---
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
    # Добавим символ новой строки в маппинг
    freq_map['\n'] = FREQ_NEWLINE
    freq_map['\r'] = FREQ_NEWLINE # И возврат каретки, если нужно
    return freq_map

FREQ_MAP = create_frequency_map()

# --- Функция генерации звука ---
def generate_tone(frequency, duration, envelope_func):
    length = int(duration * SAMPLE_RATE)
    t = np.linspace(0, duration, length, endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    envelope = envelope_func(length, SAMPLE_RATE)
    min_len = min(len(envelope), len(wave))
    envelope = envelope[:min_len]
    wave = wave[:min_len]
    return wave * envelope

# --- Функция воспроизведения звука ---
def play_tone(tone_array):
    sd.play(tone_array, samplerate=SAMPLE_RATE)
    sd.wait()

# --- Функция кодирования строки ---
def encode_text_to_sound(text):
    for char in text:
        # Обработка специальных символов, если нужно
        if char in ('\n', '\r'):
             # Генерируем и воспроизводим звук для новой строки
             tone = generate_tone(FREQ_MAP[char], DURATION_SEC, envelope_flat) # Используем плоскую огибающую
             play_tone(tone)
             continue # Переходим к следующему символу

        if char not in FREQ_MAP:
            # print(f"Предупреждение: Символ '{char}' не найден в алфавите. Пропускаю.") # Закомментим для TTY
            continue

        frequency = FREQ_MAP[char]
        envelope_func = envelope_flat
        if char.isalpha() or char in cyrillic_upper or char in cyrillic_lower:
            if char.isupper() or char in cyrillic_upper:
                envelope_func = envelope_attack
            else:
                envelope_func = envelope_decay
        else:
            envelope_func = envelope_flat

        tone = generate_tone(frequency, DURATION_SEC, envelope_func)
        # print(f"Воспроизводится символ '{char}' -> freq={frequency:.2f}Hz, env={envelope_func.__name__}") # Закомментим для TTY
        play_tone(tone)

# --- Функция фильтрации ANSI escape sequences ---
def remove_ansi_escape_sequences(text):
    """Удаляет ANSI escape sequences из строки."""
    ansi_escape_pattern = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape_pattern.sub('', text)

# --- Функция озвучки вывода ---
def speak_output(output_text):
    """Озвучивает текст вывода."""
    # Импортируем необходимые модули
    import sys
    import time
    import re
    
    # Проверяем, не является ли этот текст дубликатом последнего
    if not hasattr(speak_output, 'last_output'):
        speak_output.last_output = ""
        speak_output.last_time = 0
    
    # Проверяем, совпадает ли текущий вывод с предыдущим
    # и прошло ли достаточно времени с предыдущего вызова
    current_time = time.time()
    is_duplicate = (output_text == speak_output.last_output and 
                    (current_time - speak_output.last_time) < 0.1)  # 100 мс
    
    # Обновляем последние значения
    speak_output.last_output = output_text
    speak_output.last_time = current_time
    
    # Если это дубликат, пропускаем озвучку
    if is_duplicate:
        return
    
    # Фильтруем служебные символы и приглашения командной строки
    # Удаляем ANSI escape sequences
    clean_text_for_speech = remove_ansi_escape_sequences(output_text)
    
    # Удаляем символы новой строки, если они не нужны как звук
    clean_text = clean_text_for_speech.replace('\n', '').replace('\r', '')
    
    # Пропускаем озвучку, если текст содержит только пробелы или является приглашением командной строки
    if not clean_text.strip():
        return  # Не озвучиваем пустые строки
    
    # Пропускаем озвучку, если текст похож на приглашение командной строки
    # Обычно приглашения содержат символы вроде $, %, #, > или имя пользователя
    prompt_patterns = [
        r'^[\w\-@.:~#$%>+]+$',  # Обычные приглашения типа user@host:~$
        r'^[\w\-@.:~#$%>+]+\s*[\$\%\#\>\)]\s*$',  # Приглашения с завершающим символом
        r'^\(\w+\)\s+[\w\-@.:~#$%>+]+\s*[\$\%\#\>\)]\s*'  # Приглашения с префиксом (например, (env) user@host$)
    ]
    
    for pattern in prompt_patterns:
        if re.match(pattern, clean_text.strip()):
            return  # Не озвучиваем приглашения командной строки
    
    # Также фильтруем короткие последовательности, которые могут быть служебными символами
    if len(clean_text.strip()) < 2 and not clean_text.strip().isalnum():
        return  # Не озвучиваем короткие служебные символы
    
    encode_text_to_sound(clean_text)

# --- Функция озвучки ввода (опционально) ---
def speak_input(input_char):
    """Озвучивает один введенный символ."""
    # Удаляем символы управления, если они передаются (например, backspace)
    if input_char in ('\x7f', '\x08'): # Backspace (DEL или BS)
        # Можно озвучить специальным звуком или просто пропустить
        print("\b \b", end='', flush=True) # Визуально стираем символ ввода, если он был напечатан
        return
    if ord(input_char) < 32: # Управляющие символы (Ctrl+...)
        # Пропускаем или озвучиваем особым образом
        return
    encode_text_to_sound(input_char)