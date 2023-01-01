crypted_text = open("task4_crypted.txt", "r")
text_ = crypted_text.readline()
print(text_)
crypted_text.close()


def decoding(some_text):
    decoding = ''
    i = 0

    while i < len(some_text):
        count = 0
        if str(some_text[i]).isdigit() and not str(some_text[i + 1]).isdigit():
            count += int(some_text[i])
            decoding += some_text[i + 1] * count
            i += count
        elif str(some_text[i]).isdigit() and str(some_text[i + 1]).isdigit():
            count += int(some_text[i])
            decoding += some_text[i + 1] * count
            i += count
        else: i += 1
    return decoding

print(decoding(text_))

with open('task4_decoded_text.txt', 'w') as decoded:
    decoded.write(decoding(text_))

decoded.close()