slovo = input("Введите слово: ")

first_a_index = slovo.find('а')
last_o_index = slovo.rfind('о')

if first_a_index != -1 and last_o_index != -1:
    word_list = list(slovo)
    word_list[first_a_index],
    word_list[last_o_index] = word_list[last_o_index],
    word_list[first_a_index]
    modified_word = ''.join(word_list)
else:
    modified_word = slovo

print("Измененное слово:", modified_word)
