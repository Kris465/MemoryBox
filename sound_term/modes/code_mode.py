"""
Code mode - converts code to sound patterns
"""

import re
from ..audio.engine import AudioEngine
from ..config.sound_map import SPECIAL_SEQUENCES


class CodeMode:
    """
    Mode for handling code content using sound patterns
    """
    
    def __init__(self):
        self.audio_engine = AudioEngine()
        
    def detect_code_content(self, content):
        """
        Detect if content is code that should be converted to sound patterns
        
        Args:
            content (str): Content to analyze
            
        Returns:
            bool: True if content should be treated as code
        """
        if not content.strip():
            return False
            
        # Check if content contains programming elements
        code_indicators = [
            '=', '==', '!=', '<', '>', '<=', '>=',  # operators
            '{', '}', '[', ']', '(', ')',           # brackets
            ';', ':', ',',                         # punctuation
            'def', 'class', 'import', 'return',    # keywords
            'if', 'else', 'elif', 'for', 'while',  # control flow
            '+', '-', '*', '/', '%',               # arithmetic
            'var', 'int', 'str', 'bool',          # type hints
        ]
        
        content_lower = content.lower()
        code_matches = sum(1 for indicator in code_indicators if indicator in content_lower)
        
        # If we find at least 2 code indicators, treat as code
        return code_matches >= 2
    
    def play_special_sequence(self, sequence):
        """
        Play a special sequence with its designated sound pattern
        
        Args:
            sequence (str): Special sequence to play
        """
        if sequence in SPECIAL_SEQUENCES:
            seq_data = SPECIAL_SEQUENCES[sequence]
            freq = seq_data['frequency']
            duration = seq_data['duration']
            waveform = seq_data['waveform']
            pattern = seq_data['pattern']
            
            # Play the pattern based on its type
            if pattern == 'single':
                self.audio_engine.play_tone(freq, duration, waveform)
            elif pattern == 'double':
                self.audio_engine.play_tone(freq, duration, waveform)
                self.audio_engine.play_tone(freq, duration, waveform)
            elif pattern == 'triple':
                self.audio_engine.play_tone(freq, duration, waveform)
                self.audio_engine.play_tone(freq, duration, waveform)
                self.audio_engine.play_tone(freq, duration, waveform)
    
    def play_code_content(self, content):
        """
        Convert code content to sound patterns
        
        Args:
            content (str): Code content to convert
        """
        # Look for special sequences and replace them with special sounds
        # while preserving the rest as individual characters
        
        # Sort special sequences by length (longest first) to avoid partial matches
        sorted_sequences = sorted(SPECIAL_SEQUENCES.keys(), key=len, reverse=True)
        
        # Tokenize the content while preserving special sequences
        tokens = []
        i = 0
        while i < len(content):
            matched = False
            for seq in sorted_sequences:
                if content[i:].lower().startswith(seq):
                    # Check if it's a whole word (not part of a larger word)
                    if (i == 0 or not content[i-1].isalnum()) and \
                       (i+len(seq) >= len(content) or not content[i+len(seq)].isalnum()):
                        tokens.append(('special', seq))
                        i += len(seq)
                        matched = True
                        break
            
            if not matched:
                tokens.append(('char', content[i]))
                i += 1
        
        # Play each token
        for token_type, token_value in tokens:
            if token_type == 'special':
                self.play_special_sequence(token_value)
            else:
                self.audio_engine.play_char_sound(token_value)