'''
This module writes the text of chapter into the txt file
'''

def write(text, file_name):
    with open(f"projects/{file_name}.txt", "w", encoding="utf-8") as file:
        file.write(text)
