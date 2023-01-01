# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text_in_file = open('task4.txt', 'r')
text_ = text_in_file.readline()
print(text_)
text_in_file.close()

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


print(encrypt(text_))

with open('task4_crypted.txt', 'w') as encrypting:
    encrypting.write(encrypt(text_))

encrypting.close()
    