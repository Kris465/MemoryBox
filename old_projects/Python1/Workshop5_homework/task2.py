# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def main_func():
    text_file = input("Enter the name of the file with the text: ")
    user_message = input("Input the string that you want to record: ")
    creating_writing(text_file, user_message)

    record_file = input("Enter the file name to record: ")
    treasure = reading_file(text_file)
    crypted_text = encrypt(treasure)
    creating_writing(record_file, crypted_text)

    decode_file = input("Enter the name of the file to decode: ")
    secret_treasure = reading_file(record_file)
    normal_text = decorder(secret_treasure)
    creating_writing(decode_file, normal_text)


def creating_writing(name, message):
    creation = open(name, "w")
    creation.write(message)
    print(message)
    creation.close() 

def reading_file(name):
    with open(name, "r") as using_file:
        line = using_file.readline()
    print(line)
    using_file.close()
    return line

def encrypt(some_text):
    encrypting = ""
    count = 1
    p_char = ""

    if not some_text: return ''

    for char in some_text:
        if char != p_char:
            if p_char:
                encrypting += str(count) + p_char
            count = 1
            p_char = char
        else:
            count += 1
    else:
        encrypting += str(count) + p_char
        return encrypting

def decorder(some_text):
    ls = []
    magic_lst = []

    for i in some_text:
        if i.isdigit():
            ls.append(i)
        else:
            ls.append(i + " ")

    new_string = "".join(ls)

    new_lst = new_string.split()
    
    for i in new_lst:
        l = len(i)
        magic_lst.append(i[-1] * int(i[:l-1]))

    return "".join(magic_lst)

main_func()
