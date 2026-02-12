#!/usr/bin/env python3
"""
Test script for mixed language handling in RHVoice
"""

from sound_term.audio.rhvoice_handler import RHVoiceHandler


def test_mixed_language():
    """
    Test the mixed language functionality
    """
    rhvoice = RHVoiceHandler()
    
    # Test mixed language text
    mixed_text = "Hello мир! How are дела? This is English and это русский."
    
    print("Testing mixed language text:")
    print(f"Text: {mixed_text}")
    print("Speaking with mixed language support...")
    
    # This will use the mixed language functionality
    rhvoice.speak_text(mixed_text, lang=None)


def main():
    """
    Main test function
    """
    try:
        test_mixed_language()
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")


if __name__ == "__main__":
    main()