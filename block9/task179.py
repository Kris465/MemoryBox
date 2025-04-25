words = ["первое", "второе", "третье", "око", "дед"]


words_a = [word for word in words if len(set(word)) == len(word)]
print("а)", words_a)


words_b = [word for word in words if word == word[::-1]]
print("б)", words_b)
