sentence = input()

index = sentence.index(',')
count_n = sentence[:index].count('н')
print(count_n)

index = sentence.find(',')
if index != -1:
    count_n = sentence[:index].count('н')
else:
    count_n = sentence.count('н')
print(count_n)
