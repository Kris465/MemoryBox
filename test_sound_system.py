#!/usr/bin/env python3
"""
Test script for sound generation system
"""

from sound_term.audio.engine import AudioEngine
from sound_term.modes.text_mode import TextMode
from sound_term.modes.code_mode import CodeMode


def test_sound_generation():
    """
    Test the sound generation system with various characters
    """
    print("Testing Sound Generation System...")
    
    audio_engine = AudioEngine()
    
    # Test individual characters
    print("\n1. Testing individual characters:")
    test_chars = "abcdefghij0123456789!@#$%^&*()"
    
    for char in test_chars:
        print(f"Playing sound for: '{char}'")
        audio_engine.play_char_sound(char)
    
    # Test special symbols
    print("\n2. Testing special symbols:")
    special_chars = "()[]{}|\\:;\"'<>?,./"
    
    for char in special_chars:
        print(f"Playing sound for: '{char}'")
        audio_engine.play_char_sound(char)
    
    # Test whitespace
    print("\n3. Testing whitespace:")
    whitespace = " \t\n"
    
    for i, char in enumerate(whitespace):
        names = ["space", "tab", "newline"]
        print(f"Playing sound for: {names[i]}")
        audio_engine.play_char_sound(char)
    
    # Test sequences at different speeds
    print("\n4. Testing sequences at different speeds:")
    
    test_sequences = [
        "hello",
        "def func():",
        "for i in range(10):",
        "print('test')",
        "if x == 5:"
    ]
    
    speeds = [10, 15, 17]  # Characters per second
    
    for seq in test_sequences:
        for speed in speeds:
            print(f"\nPlaying sequence '{seq}' at {speed} chars/sec:")
            audio_engine.play_code_sequence(seq, chars_per_second=speed)


def test_modes():
    """
    Test the text and code modes
    """
    print("\n\nTesting Modes...")
    
    text_mode = TextMode()
    code_mode = CodeMode()
    
    # Test text detection
    print("\n1. Testing text detection:")
    text_samples = [
        "This is a sample text in English.",
        "Это пример текста на русском языке.",
        "Hello world, this is a text sample."
    ]
    
    for sample in text_samples:
        is_text = text_mode.detect_text_content(sample)
        print(f"'{sample}' -> Detected as text: {is_text}")
    
    # Test code detection
    print("\n2. Testing code detection:")
    code_samples = [
        "def hello():\n    print('world')",
        "for i in range(10):\n    if i % 2 == 0:\n        print(i)",
        "int x = 5;\nif(x > 3) {\n    printf('hello');\n}"
    ]
    
    for sample in code_samples:
        is_code = code_mode.detect_code_content(sample)
        print(f"Code sample -> Detected as code: {is_code}")


def main():
    """
    Main test function
    """
    print("Sound Terminal - Testing Suite")
    print("="*40)
    
    try:
        test_sound_generation()
        test_modes()
        
        print("\n" + "="*40)
        print("Testing completed!")
        
    except KeyboardInterrupt:
        print("\nTesting interrupted by user.")
    except Exception as e:
        print(f"\nError during testing: {e}")


if __name__ == "__main__":
    main()