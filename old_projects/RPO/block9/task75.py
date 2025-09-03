sentence = input("Введите предложение: ")

index = sentence.index(',')
print("а)", sentence[:index])

index = sentence.find(',')
if index != -1:
    print("б)", sentence[:index])
else:
    print("б)", sentence)
