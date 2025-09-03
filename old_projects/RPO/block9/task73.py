sentence = input()
index_c = sentence.rfind('с')
index_t = sentence.rfind('Т')
if index_c > index_t:
    print('с')
elif index_t > index_c:
    print('Т')
else:
    print('Обе буквы отсутствуют или встречаются в одном месте')
