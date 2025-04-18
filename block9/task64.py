def count_adjacent_duplicates(sentence):
    count = 0
    for i in range(len(sentence) - 1):
        if sentence[i] == sentence[i + 1]:
            count += 1
    return count


sentence = "hello"
print(count_adjacent_duplicates(sentence))
