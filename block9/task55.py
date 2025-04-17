sentence = "Пример предложения с символами п и c."
char1, char2 = "п", "с"
for chair in sentence:
    if chair in (char1, char2):
        print(char1)
