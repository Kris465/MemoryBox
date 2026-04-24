# config.py
"""Конфигурация для wst — звукового интерфейса терминала."""

# --- Звук ---
SAMPLE_RATE = 44100       # Частота дискретизации
DURATION_CHAR = 0.5       # Длительность одного символа (сек)
DURATION_LINE_PAUSE = 0.15  # Пауза между строками вывода

# --- Диапазоны частот ---
# Буквы: 400-1200 Гц — приятный музыкальный диапазон
FREQ_RANGE_LETTERS_LOW = 400
FREQ_RANGE_LETTERS_HIGH = 1200

# Цифры: 300-400 Гц — чуть ниже букв, легко отличить
FREQ_RANGE_DIGITS_LOW = 300
FREQ_RANGE_DIGITS_HIGH = 400

# Символы: 1500-2000 Гц — выше, выделяются
FREQ_RANGE_SYMBOLS_LOW = 1500
FREQ_RANGE_SYMBOLS_HIGH = 2000

# Спецсимволы
FREQ_NEWLINE = 2500       # Высокий сигнал — сразу слышно новую строку
FREQ_CARRIAGE_RETURN = 2300
FREQ_TAB = 1300           # Звук таба

# --- Звуковые маркеры ---
FREQ_MARKER_BLOCK_START = 2000  # Начало нового блока вывода
FREQ_MARKER_BLOCK_END = 800     # Конец блока
FREQ_MARKER_ERROR = 400         # Ошибка (низкий тон)
FREQ_MARKER_SUCCESS = 1200      # Успех (высокий тон)

# --- Режимы ---
MODE_COMMAND = "command"  # Полный вывод тонами
MODE_TUI = "tui"          # Только активная строка + события
MODE_STREAM = "stream"    # Каждая строка по мере появления

DEFAULT_MODE = MODE_COMMAND

# --- Огибающие ---
ENVELOPE_ATTACK_MS = 15   # Нарастание для заглавных
ENVELOPE_DECAY_MS = 30    # Затухание для строчных
