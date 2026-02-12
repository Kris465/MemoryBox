"""
Audio engine combining RHVoice and custom sound generation
"""

import numpy as np
import sounddevice as sd
from .rhvoice_handler import RHVoiceHandler
from ..config.sound_map import SOUND_MAP


class AudioEngine:
    """
    Main audio engine that handles both RHVoice for text
    and custom sound generation for code
    """
    
    def __init__(self):
        self.rhvoice = RHVoiceHandler()
        self.sample_rate = 44100
        self.volume = 0.3
        
    def _generate_waveform(self, frequency, duration, waveform='sine', attack=0.01, decay=0.01):
        """
        Generate a waveform with specific characteristics
        
        Args:
            frequency (float): Frequency in Hz
            duration (float): Duration in seconds
            waveform (str): Type of waveform ('sine', 'square', 'sawtooth', 'impulse', 'noise', 'pulse')
            attack (float): Attack time in seconds
            decay (float): Decay time in seconds
        """
        if duration <= 0:
            # Handle special cases like spaces
            sd.sleep(int(0.02 * 1000))  # 20ms pause
            return np.array([])
            
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        
        if waveform == 'sine':
            wave = np.sin(2 * np.pi * frequency * t)
        elif waveform == 'square':
            wave = np.sign(np.sin(2 * np.pi * frequency * t))
        elif waveform == 'sawtooth':
            wave = 2 * (t * frequency - np.floor(0.5 + t * frequency))
        elif waveform == 'impulse':
            # Sharp impulse sound
            wave = np.exp(-t * 10) * np.sin(2 * np.pi * frequency * t)
        elif waveform == 'noise':
            # Band-limited noise centered at frequency
            wave = np.random.normal(0, 1, len(t)) * np.sin(2 * np.pi * frequency * t)
            # Apply envelope to make it shorter
            envelope = np.exp(-t * 15)
            wave *= envelope
        elif waveform == 'pulse':
            # Short pulse
            wave = np.zeros_like(t)
            pulse_duration = min(0.01, duration)  # 10ms max
            pulse_samples = int(pulse_duration * self.sample_rate)
            wave[:pulse_samples] = np.sin(2 * np.pi * frequency * t[:pulse_samples])
        else:
            wave = np.sin(2 * np.pi * frequency * t)
        
        # Apply ADSR envelope (Attack, Decay, Sustain, Release)
        total_samples = len(wave)
        attack_samples = int(attack * self.sample_rate)
        decay_samples = int(decay * self.sample_rate)
        
        # Ensure we don't exceed array bounds
        attack_samples = min(attack_samples, total_samples // 3)
        decay_samples = min(decay_samples, total_samples // 3)
        
        # Create envelope
        envelope = np.ones(total_samples)
        
        # Attack phase
        if attack_samples > 0:
            envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
        
        # Decay phase
        if decay_samples > 0:
            envelope[attack_samples:attack_samples+decay_samples] = np.linspace(1, 0.7, decay_samples)
        
        # Apply envelope
        wave *= envelope
        
        return wave
    
    def play_tone(self, frequency, duration, waveform='sine', attack=0.01, decay=0.01):
        """
        Generate and play a tone
        
        Args:
            frequency (float): Frequency in Hz
            duration (float): Duration in seconds
            waveform (str): Type of waveform ('sine', 'square', 'sawtooth', 'impulse', 'noise', 'pulse')
            attack (float): Attack time in seconds
            decay (float): Decay time in seconds
        """
        wave = self._generate_waveform(frequency, duration, waveform, attack, decay)
        
        if len(wave) > 0:
            # Apply volume
            wave *= self.volume
            
            # Play the sound
            sd.play(wave, samplerate=self.sample_rate)
            sd.wait()  # Wait until the sound finishes playing
        else:
            # Just a pause if no waveform was generated
            sd.sleep(int(duration * 1000))
    
    def play_char_sound(self, char):
        """
        Play the sound associated with a character
        
        Args:
            char (str): Character to play sound for
        """
        char_lower = char.lower()
        
        if char_lower in SOUND_MAP:
            sound_config = SOUND_MAP[char_lower]
            
            if 'frequency' in sound_config:
                self.play_tone(
                    frequency=sound_config['frequency'],
                    duration=sound_config['duration'],
                    waveform=sound_config.get('waveform', 'sine'),
                    attack=sound_config.get('attack', 0.01),
                    decay=sound_config.get('decay', 0.01)
                )
            else:
                # Just a pause (for space, tab, newline)
                duration = sound_config.get('duration', 0.02)
                sd.sleep(int(duration * 1000))
        else:
            # Unknown character - play a default sound
            self.play_tone(frequency=400, duration=0.05, waveform='sine')
    
    def play_sequence_with_timing(self, sequence, chars_per_second=15):
        """
        Play a sequence of characters with precise timing
        
        Args:
            sequence (str): Sequence of characters to play
            chars_per_second (int): Target playback speed in characters per second
        """
        import time
        interval = 1.0 / chars_per_second  # Time interval between characters
        
        for char in sequence:
            start_time = time.time()
            
            self.play_char_sound(char)
            
            # Calculate elapsed time and sleep for the remainder
            elapsed = time.time() - start_time
            remaining = max(0, interval - elapsed)
            
            if remaining > 0:
                sd.sleep(int(remaining * 1000))
    
    def speak_text(self, text, lang="ru"):
        """
        Speak text using RHVoice
        
        Args:
            text (str): Text to speak
            lang (str): Language ('ru' for Russian, 'en' for English)
        """
        self.rhvoice.speak_text(text, lang)
    
    def play_code_sequence(self, code_string, chars_per_second=15):
        """
        Play a sequence of sounds for a code string with specified speed
        
        Args:
            code_string (str): String of code to convert to sounds
            chars_per_second (int): Playback speed in characters per second
        """
        self.play_sequence_with_timing(code_string, chars_per_second)