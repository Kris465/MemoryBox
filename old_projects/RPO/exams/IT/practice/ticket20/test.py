import re


string = 'aaa asdas asds'
print(re.search('asdas', string))
print(re.fullmatch('aaa', string))
print(re.split('asds', string, maxsplit=0))
print(re.split('asdas', string, maxsplit=0))
print(re.split('aaa', string, maxsplit=0))
print(re.findall('aaa', string))
print(re.findall('asdas', string))
print(re.findall('asds', string))
print(re.finditer('asdas', string))
print(re.sub('aaa', 'dasdas', string, count=0))

# log(5) + 30

