"""
Main entry point for Sound Terminal
"""

from sound_term.terminal.handler import TerminalHandler
from sound_term.audio.engine import AudioEngine


def main():
    """
    Main function to start the Sound Terminal
    """
    print("Starting Sound Terminal...")
    print("This will create an audio interface for your terminal")
    print("Press Ctrl+C to exit")
    
    try:
        # Initialize the terminal handler
        term_handler = TerminalHandler()
        
        # Example: Process some sample content
        sample_text = "Hello, this is a sample text in Russian: Привет мир!"
        sample_code = "def hello_world():\n    print('Hello, world!')"
        
        print("\nPlaying sample text:")
        term_handler.process_output(sample_text)
        
        print("\nPlaying sample code:")
        term_handler.process_output(sample_code)
        
        # Start an actual terminal session
        print("\nStarting interactive terminal session...")
        print("All terminal output will be converted to audio.")
        print("Code will be played as sound patterns, text as speech.")
        term_handler.start_terminal_session()
        
    except KeyboardInterrupt:
        print("\nSound Terminal stopped by user.")


if __name__ == "__main__":
    main()