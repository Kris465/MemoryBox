def rotate_word_with_loop(word, k):
    rotated = list(word)

    for _ in range(k):
        first_char = rotated.pop(0)
        rotated.append(first_char)

    return ''.join(rotated)


word = 'абракадабра'
k = 3
result = rotate_word_with_loop(word, k)
print(result)
