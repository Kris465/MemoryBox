import re

text = input()
sentences = re.split(r'[.!?]+', text.strip())
first_sentence = sentences[0]

count_i_1 = first_sentence.count('и')
print(count_i_1)

count_i_2 = first_sentence.count('и')
print(count_i_2)
