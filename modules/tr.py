from reader_from_json import read
from translator_class import Translator
from writer_to_txt import write_txt

title = input("Title: ")
chapter = input("Chapter: ")
project = read(title)
text = project[chapter]
write_txt(chapter, text)
max_length = 10000
substrings = []

while len(text) > max_length:
    index = text.rfind(".", 0, max_length)
    if index == -1:
        index = max_length
        substrings.append(text[:index+1])
        text = text[index+1:]
        print(text)
    substrings.append(text)
    print(substrings)
    translator = Translator()
    for string in substrings:
        part = translator.translate(string)
        write_txt(chapter, part)
