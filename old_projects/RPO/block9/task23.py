def get_substring(word, m, n):

    if m < 0 or n >= len(word) or m > n:
        return "Некорректные индексы"

    return word[m:n+1]


word = "Программирование"
m = 3
n = 7
substring = get_substring(word, m, n)
print(substring)
