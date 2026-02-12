"""
RHVoice handler module
"""

import subprocess
import os
import re


class RHVoiceHandler:
    """
    Handler for RHVoice text-to-speech engine
    """
    
    def __init__(self):
        self.default_russian_voice = "Anna"
        self.default_english_voice = "Alan"
        self.rate = 1.0      # Normal speed
        self.pitch = 1.0     # Normal pitch
        self.volume = 1.0    # Normal volume
        
    def detect_language(self, text):
        """
        Detect language in text (Russian, English or mixed)
        
        Args:
            text (str): Text to analyze
            
        Returns:
            str: 'ru', 'en', or 'mixed'
        """
        # Count Cyrillic and Latin characters
        cyrillic_count = len(re.findall(r'[а-яё]', text.lower()))
        latin_count = len(re.findall(r'[a-z]', text.lower()))
        total_letters = cyrillic_count + latin_count
        
        if total_letters == 0:
            return 'en'  # Default to English if no letters found
            
        cyrillic_ratio = cyrillic_count / total_letters
        latin_ratio = latin_count / total_letters
        
        # If both languages present significantly, return mixed
        if cyrillic_ratio > 0.1 and latin_ratio > 0.1:
            return 'mixed'
        elif cyrillic_ratio > latin_ratio:
            return 'ru'
        else:
            return 'en'
    
    def speak_mixed_text(self, text):
        """
        Speak text with mixed languages using appropriate voices per segment
        
        Args:
            text (str): Text to speak
        """
        # Split text into segments by language
        import re
        
        # This regex splits text into segments of Cyrillic and Latin words
        # It preserves spaces and punctuation between words
        segments = re.split(r'(\s+|[,.!?;:])', text)
        
        for segment in segments:
            if not segment.strip():  # Skip empty segments (whitespace)
                continue
                
            # Detect language of this segment
            segment_lang = self.detect_language(segment)
            
            if segment_lang == 'ru':
                voice = self.default_russian_voice
            else:  # en
                voice = self.default_english_voice
            
            # Skip non-text segments (punctuation, spaces) or speak them with default voice
            if re.match(r'^[\s,.!?;:]+$', segment):
                # For simplicity, we'll use the English voice for punctuation
                # but in a more advanced version, we could handle this differently
                voice = self.default_english_voice
            
            cmd = [
                "RHVoice-test",
                "-p", voice,  # voice profile
                "-r", str(int(self.rate * 100)),  # rate percentage
                "-t", str(int(self.pitch * 100)),  # pitch percentage
                "-v", str(int(self.volume * 100))  # volume percentage
            ]
            
            # Execute command
            process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate(input=segment)
            
            if process.returncode != 0:
                print(f"RHVoice error for segment '{segment}': {stderr}")
    
    def speak_text(self, text, lang=None):
        """
        Speak text using RHVoice
        
        Args:
            text (str): Text to speak
            lang (str): Language ('ru' for Russian, 'en' for English, or None for auto-detect)
        """
        try:
            if lang is None:
                lang = self.detect_language(text)
            
            if lang == 'mixed':
                self.speak_mixed_text(text)
            else:
                # Set voice based on language
                if lang == "ru":
                    voice = self.default_russian_voice  # Russian female voice
                else:
                    voice = self.default_english_voice  # English male voice

                # For RHVoice-test, we need to pass text via stdin
                cmd = [
                    "RHVoice-test",
                    "-p", voice,  # voice profile
                    "-r", str(int(self.rate * 100)),  # rate percentage
                    "-t", str(int(self.pitch * 100)),  # pitch percentage
                    "-v", str(int(self.volume * 100))  # volume percentage
                ]

                # Execute command
                process = subprocess.Popen(
                    cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                stdout, stderr = process.communicate(input=text)

                if process.returncode != 0:
                    print(f"RHVoice error: {stderr}")

        except FileNotFoundError:
            print("RHVoice-test not found. Please install RHVoice.")
        except Exception as e:
            print(f"Error speaking text: {e}")

    def set_voice_params(self, rate=1.0, pitch=1.0, volume=1.0):
        """
        Set voice parameters

        Args:
            rate (float): Speech rate (0.1-10.0)
            pitch (float): Pitch (0.1-10.0)
            volume (float): Volume (0.0-10.0)
        """
        self.rate = rate
        self.pitch = pitch
        self.volume = volume