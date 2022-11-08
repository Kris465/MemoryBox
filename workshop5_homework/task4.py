# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text_in_file = open('task4.txt', 'r')
text_ = text_in_file.readline()
print(text_)
text_in_file.close()

def encrypt(some_text):
    encrypting = ""
    # i = 0
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

    # while i < len(some_text):
    #     count = 1
    #     while i + 1 < len(some_text) and some_text[i] == some_text[i + 1]:
    #         count += 1
    #         i += 1
    #     encrypting += str(count) + some_text[i]
    #     i += 1
    # return encrypting

print(encrypt(text_))

with open('task4_crypted.txt', 'w') as encrypting:
    encrypting.write(encrypt(text_))

encrypting.close()
    