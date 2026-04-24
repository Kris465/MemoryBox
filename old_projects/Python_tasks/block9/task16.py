word = input("Введите слово: ")
if word[1] == word[3]:
    print(f"В слове {word} буквы {word[1]}, {word[3]} одинаковы")
else:
    print(f"В слове {word} буквы {word[1]}, {word[3]} не одинаковы")
