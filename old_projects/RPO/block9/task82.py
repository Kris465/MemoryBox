sentence = input().lstrip()
first_word = sentence.split(' ')[0]
count_o = first_word.lower().count('о')
print(count_o)
