word = "программирование"
letter_counts = {}


for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1


duplicates = [letter for letter, count in letter_counts.items() if count >= 2]

print("Буквы, встречающиеся два или более раз:", duplicates)
