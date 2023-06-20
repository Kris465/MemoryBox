import os


def replace_spaces_in_file(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        content = f.read()

    new_content = content.replace('	', '\n')
    with open("cut_" + filename, 'a', encoding="UTF-8") as f:
        f.write(new_content)


def process_text_files(directory):
    files = os.listdir(directory)
    text_files = [f for f in files if f.endswith('.txt')]
    for filename in text_files:
        replace_spaces_in_file(filename)


process_text_files('C:/Users/Nata/Prog/Pars/modules')
