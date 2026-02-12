"""
Terminal handler - captures and processes terminal output
"""

import pty
import os
import select
import subprocess
from ..modes.text_mode import TextMode
from ..modes.code_mode import CodeMode


class TerminalHandler:
    """
    Handles terminal output and routes to appropriate audio mode
    """
    
    def __init__(self):
        self.text_mode = TextMode()
        self.code_mode = CodeMode()
        self.buffer = ""
        
    def determine_content_type(self, content):
        """
        Determine if content is text or code
        
        Args:
            content (str): Content to analyze
            
        Returns:
            str: 'text' or 'code'
        """
        # Check if it looks more like text
        if self.text_mode.detect_text_content(content):
            return 'text'
        
        # Check if it looks more like code
        if self.code_mode.detect_code_content(content):
            return 'code'
        
        # Default to code mode for terminal output (commands, paths, etc.)
        # This ensures that even simple commands like 'ls', 'pwd' are treated as code
        return 'code'
    
    def process_output(self, output):
        """
        Process terminal output and convert to appropriate audio
        
        Args:
            output (str): Raw terminal output to process
        """
        content_type = self.determine_content_type(output)
        
        if content_type == 'text':
            # Use RHVoice for text content
            self.text_mode.speak_content(output)
        else:
            # Use sound patterns for code/content
            self.code_mode.play_code_content(output)
    
    def start_terminal_session(self, command="/bin/bash"):
        """
        Start a terminal session and capture output
        
        Args:
            command (str): Command to run in terminal (default: bash)
        """
        # Create a pseudo-terminal
        master, slave = pty.openpty()
        
        # Start the subprocess
        proc = subprocess.Popen(
            command,
            stdin=slave,
            stdout=slave,
            stderr=slave,
            universal_newlines=True
        )
        
        # Close the slave end in the parent process
        os.close(slave)
        
        print(f"Interactive terminal started with PID {proc.pid}. Type commands and see output as audio.")
        print("Press Ctrl+D or type 'exit' to quit.")
        
        try:
            while proc.poll() is None:
                # Wait for data to be available
                ready, _, _ = select.select([master], [], [], 0.1)
                
                if ready:
                    try:
                        data = os.read(master, 1024).decode('utf-8', errors='ignore')
                        if data:
                            self.process_output(data)
                    except OSError:
                        # Terminal closed
                        break
        finally:
            # Clean up
            os.close(master)
            proc.terminate()
            proc.wait()
            
        print("Terminal session ended.")