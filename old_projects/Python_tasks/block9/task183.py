def unique_words_in_one_sentence(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    set1 = set(words1)
    set2 = set(words2)

    diff_set = set1 ^ set2

    result = []
    for word in diff_set:
        count1 = words1.count(word)
        count2 = words2.count(word)
        if count1 > 0 and count2 == 0:
            result.extend([word]*count1)
        elif count2 > 0 and count1 == 0:
            result.extend([word]*count2)

    return result


sentence1 = input("Введите первое предложение: ")
sentence2 = input("Введите второе предложение: ")
result = unique_words_in_one_sentence(sentence1, sentence2)
print(result)
