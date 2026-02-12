"""
Configuration for sound mappings
"""

# Sound mapping for code mode
SOUND_MAP = {
    # Vowels - pure sine tones
    'a': {'frequency': 440, 'duration': 0.04, 'waveform': 'sine', 'attack': 0.005, 'decay': 0.01},  # A
    'e': {'frequency': 523, 'duration': 0.04, 'waveform': 'sine', 'attack': 0.005, 'decay': 0.01},  # C
    'i': {'frequency': 587, 'duration': 0.04, 'waveform': 'sine', 'attack': 0.005, 'decay': 0.01},  # D
    'o': {'frequency': 659, 'duration': 0.04, 'waveform': 'sine', 'attack': 0.005, 'decay': 0.01},  # E
    'u': {'frequency': 698, 'duration': 0.04, 'waveform': 'sine', 'attack': 0.005, 'decay': 0.01},  # F
    'y': {'frequency': 784, 'duration': 0.04, 'waveform': 'sine', 'attack': 0.005, 'decay': 0.01},  # G
    
    # Consonants - square or pulse waves
    'b': {'frequency': 220, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'c': {'frequency': 262, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'd': {'frequency': 294, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'f': {'frequency': 330, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'g': {'frequency': 349, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'h': {'frequency': 392, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'j': {'frequency': 415, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'k': {'frequency': 440, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'l': {'frequency': 466, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'm': {'frequency': 523, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'n': {'frequency': 554, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'p': {'frequency': 587, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'q': {'frequency': 622, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'r': {'frequency': 659, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    's': {'frequency': 698, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    't': {'frequency': 740, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'v': {'frequency': 784, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'w': {'frequency': 831, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'x': {'frequency': 880, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    'z': {'frequency': 932, 'duration': 0.035, 'waveform': 'pulse', 'attack': 0.002, 'decay': 0.008},
    
    # Numbers - ascending sawtooth tones
    '0': {'frequency': 131, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # C
    '1': {'frequency': 147, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # D
    '2': {'frequency': 165, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # E
    '3': {'frequency': 175, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # F
    '4': {'frequency': 196, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # G
    '5': {'frequency': 220, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # A
    '6': {'frequency': 247, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # B
    '7': {'frequency': 262, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # C
    '8': {'frequency': 294, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # D
    '9': {'frequency': 330, 'duration': 0.04, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},  # E
    
    # Operators - impulse sounds
    '+': {'frequency': 950, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '-': {'frequency': 850, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '*': {'frequency': 1000, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '/': {'frequency': 900, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '=': {'frequency': 1050, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '!': {'frequency': 1100, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '<': {'frequency': 750, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '>': {'frequency': 800, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '&': {'frequency': 1150, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    '|': {'frequency': 1200, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.005},
    
    # Brackets - distinctive pulse sounds
    '(': {'frequency': 200, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    ')': {'frequency': 400, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    '[': {'frequency': 150, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    ']': {'frequency': 350, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    '{': {'frequency': 175, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    '}': {'frequency': 375, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    
    # Punctuation - short impulse sounds
    ',': {'frequency': 700, 'duration': 0.02, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.003},
    '.': {'frequency': 750, 'duration': 0.02, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.003},
    ':': {'frequency': 800, 'duration': 0.02, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.003},
    ';': {'frequency': 850, 'duration': 0.02, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.003},
    '?': {'frequency': 900, 'duration': 0.03, 'waveform': 'sawtooth', 'attack': 0.005, 'decay': 0.01},
    '"': {'frequency': 950, 'duration': 0.025, 'waveform': 'sine', 'attack': 0.002, 'decay': 0.005},
    "'": {'frequency': 1000, 'duration': 0.025, 'waveform': 'impulse', 'attack': 0.001, 'decay': 0.003},
    
    # Special symbols
    '@': {'frequency': 550, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '#': {'frequency': 600, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '$': {'frequency': 650, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '%': {'frequency': 700, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '^': {'frequency': 750, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '~': {'frequency': 800, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '`': {'frequency': 850, 'duration': 0.035, 'waveform': 'noise', 'attack': 0.005, 'decay': 0.01},
    '\\': {'frequency': 900, 'duration': 0.03, 'waveform': 'pulse', 'attack': 0.005, 'decay': 0.01},
    
    # Whitespace - pauses
    ' ': {'duration': 0.015},  # Short pause
    '\t': {'duration': 0.05},  # Medium pause
    '\n': {'duration': 0.08},  # Longer pause
}

# Special sequences - unique sounds for common programming constructs
SPECIAL_SEQUENCES = {
    'def': {'frequency': 300, 'duration': 0.1, 'waveform': 'sine', 'pattern': 'triple'},
    'class': {'frequency': 350, 'duration': 0.1, 'waveform': 'sine', 'pattern': 'triple'},
    'import': {'frequency': 400, 'duration': 0.1, 'waveform': 'sine', 'pattern': 'double'},
    'return': {'frequency': 450, 'duration': 0.1, 'waveform': 'sine', 'pattern': 'double'},
    'if': {'frequency': 500, 'duration': 0.08, 'waveform': 'impulse', 'pattern': 'single'},
    'else': {'frequency': 550, 'duration': 0.08, 'waveform': 'impulse', 'pattern': 'double'},
    'elif': {'frequency': 600, 'duration': 0.08, 'waveform': 'impulse', 'pattern': 'double'},
    'for': {'frequency': 650, 'duration': 0.08, 'waveform': 'impulse', 'pattern': 'single'},
    'while': {'frequency': 700, 'duration': 0.08, 'waveform': 'impulse', 'pattern': 'single'},
    'try': {'frequency': 750, 'duration': 0.08, 'waveform': 'pulse', 'pattern': 'single'},
    'except': {'frequency': 800, 'duration': 0.08, 'waveform': 'pulse', 'pattern': 'double'},
    'finally': {'frequency': 850, 'duration': 0.08, 'waveform': 'pulse', 'pattern': 'triple'},
    'with': {'frequency': 900, 'duration': 0.08, 'waveform': 'pulse', 'pattern': 'single'},
    'as': {'frequency': 950, 'duration': 0.05, 'waveform': 'impulse', 'pattern': 'single'},
    'in': {'frequency': 1000, 'duration': 0.05, 'waveform': 'impulse', 'pattern': 'single'},
    'is': {'frequency': 1050, 'duration': 0.05, 'waveform': 'impulse', 'pattern': 'single'},
    'lambda': {'frequency': 1100, 'duration': 0.1, 'waveform': 'sawtooth', 'pattern': 'double'},
    'yield': {'frequency': 1150, 'duration': 0.1, 'waveform': 'sawtooth', 'pattern': 'double'},
    'assert': {'frequency': 1200, 'duration': 0.1, 'waveform': 'sawtooth', 'pattern': 'triple'},
    'del': {'frequency': 1250, 'duration': 0.08, 'waveform': 'noise', 'pattern': 'single'},
    'global': {'frequency': 1300, 'duration': 0.1, 'waveform': 'noise', 'pattern': 'double'},
    'nonlocal': {'frequency': 1350, 'duration': 0.1, 'waveform': 'noise', 'pattern': 'double'},
    'raise': {'frequency': 1400, 'duration': 0.1, 'waveform': 'noise', 'pattern': 'triple'},
    'break': {'frequency': 1450, 'duration': 0.1, 'waveform': 'noise', 'pattern': 'triple'},
    'continue': {'frequency': 1500, 'duration': 0.1, 'waveform': 'noise', 'pattern': 'triple'},
}