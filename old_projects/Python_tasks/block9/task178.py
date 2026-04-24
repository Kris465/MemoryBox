sentence = input("Введите предложение: ")


def process_word(word):

    if 'a' in word:
        word = word.replace('a', 'o', 1)
    last_char = word[-1]
    word = word[:-1] + word[-1]
    word = word.replace(last_char, '')
    seen = set()
    new_word = []
    for char in word:
        if char not in seen:
            seen.add(char)
            new_word.append(char)
    processed_word = ''.join(new_word)

    return processed_word


def remove_middle_letters(word):
    length = len(word)
    if length % 2 == 0:
        mid_index1 = length // 2 - 1
        mid_index2 = length // 2
        return word[:mid_index1] + word[mid_index2 + 1:]
    else:
        mid_index = length // 2
        return word[:mid_index] + word[mid_index + 1:]


def process_sentence(sentence):
    words = sentence.split()
    processed_words = [process_word(word) for word in words]
    longest_word = max(processed_words, key=len)
    longest_word_processed = remove_middle_letters(longest_word)
    processed_words[
        processed_words.index(longest_word)] = longest_word_processed
    return ' '.join(processed_words)


result = process_sentence(sentence)
print(result)
