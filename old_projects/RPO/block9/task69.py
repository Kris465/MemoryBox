import re

text = input()
sentences = re.split(r'[.!?]+', text.strip())
sentences = [s for s in sentences if s.strip()]
print(len(sentences))
