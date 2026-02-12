"""
Text mode - uses RHVoice for speaking text content
"""

from ..audio.rhvoice_handler import RHVoiceHandler


class TextMode:
    """
    Mode for handling text content using RHVoice
    """
    
    def __init__(self):
        self.rhvoice = RHVoiceHandler()
        
    def detect_text_content(self, content):
        """
        Detect if content is text that should be spoken with RHVoice
        
        Args:
            content (str): Content to analyze
            
        Returns:
            bool: True if content should be treated as text
        """
        # Simple heuristic: if content contains mostly letters and spaces
        # and has common sentence structures, treat as text
        if not content.strip():
            return False
            
        # Check if content looks more like text than code
        alphanumeric_chars = sum(c.isalpha() or c.isspace() for c in content)
        total_chars = len(content)
        
        # If more than 70% are letters/spaces, likely text
        if total_chars > 0 and alphanumeric_chars / total_chars > 0.7:
            # Additional check: presence of common text elements
            text_indicators = ['.', '!', '?', ',', 'the', 'and', 'that', 'this', 'with', 'for']
            content_lower = content.lower()
            text_matches = sum(1 for indicator in text_indicators if indicator in content_lower)
            
            return text_matches > 0
        
        return False
    
    def speak_content(self, content, lang="ru"):
        """
        Speak content using RHVoice
        
        Args:
            content (str): Content to speak
            lang (str): Language ('ru' for Russian, 'en' for English)
        """
        self.rhvoice.speak_text(content, lang)