sentence = input()
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = sum(1 for c in sentence if c in vowels)
print(count)
