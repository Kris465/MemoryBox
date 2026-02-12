#!/usr/bin/env python3
"""
Test script for language detection in RHVoice
"""

from sound_term.audio.rhvoice_handler import RHVoiceHandler


def test_language_detection():
    """
    Test the language detection functionality
    """
    rhvoice = RHVoiceHandler()
    
    test_texts = [
        "This is English text",
        "Это русский текст",
        "This is English and это русский mixed together",
        "Hello мир! How are дела?",
        "Just English here",
        "Только русский язык"
    ]
    
    print("Language Detection Test:")
    print("-" * 40)
    
    for text in test_texts:
        detected_lang = rhvoice.detect_language(text)
        print(f"Text: '{text[:30]}{'...' if len(text) > 30 else ''}'")
        print(f"Detected: {detected_lang}")
        print()


def main():
    """
    Main test function
    """
    test_language_detection()


if __name__ == "__main__":
    main()