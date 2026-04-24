def rearrange_word(word, s, k):
    lst = list(word)
    lst.insert(k - 1, lst.pop(s - 1))
    return ''.join(lst)


word = "пример"
s = 5
k = 2
result = rearrange_word(word, s, k)
print(result)
