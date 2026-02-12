#!/usr/bin/env python3
"""
Demonstration script for Sound Terminal features
"""

from sound_term.audio.engine import AudioEngine
from sound_term.modes.text_mode import TextMode
from sound_term.modes.code_mode import CodeMode


def demo_features():
    """
    Demonstrate key features of Sound Terminal
    """
    print("Sound Terminal - Feature Demonstration")
    print("="*50)
    
    audio_engine = AudioEngine()
    text_mode = TextMode()
    code_mode = CodeMode()
    
    print("\n1. Individual character sounds:")
    print("   Playing sounds for letters, numbers, and symbols...")
    demo_chars = "abc123!@#()"
    for char in demo_chars:
        print(f"   Character '{char}': ", end="", flush=True)
        audio_engine.play_char_sound(char)
    
    print("\n2. Code sequence at different speeds:")
    code_seq = "def hello():\n  print('world')"
    
    for speed in [10, 15, 17]:
        print(f"   Playing at {speed} chars/sec: ", end="", flush=True)
        audio_engine.play_code_sequence(code_seq, chars_per_second=speed)
    
    print("\n3. Text vs Code detection:")
    text_sample = "This is a sample text in English language."
    code_sample = "for i in range(10):\n  if i % 2 == 0:\n    print(i)"
    
    print(f"   Text detected: '{text_sample[:20]}...' -> {text_mode.detect_text_content(text_sample)}")
    print(f"   Code detected: '{code_sample[:20]}...' -> {code_mode.detect_code_content(code_sample)}")
    
    print("\n4. Speed demonstration:")
    test_string = "hello_world"
    speeds = [10, 15, 17, 20]
    
    for speed in speeds:
        print(f"   Playing '{test_string}' at {speed} chars/sec: ", end="", flush=True)
        audio_engine.play_code_sequence(test_string, chars_per_second=speed)
    
    print("\n\nFeature demonstration completed!")


def main():
    """
    Main demo function
    """
    try:
        demo_features()
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nError during demo: {e}")


if __name__ == "__main__":
    main()