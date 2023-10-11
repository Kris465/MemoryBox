import re

chapter = '第89章 番外*圆满'
match = re.search(r'\d+', chapter)
print(match.group(1), type(match.group(0)))
