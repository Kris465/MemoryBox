def swap_first_last_word(sentence):

    words = sentence.split()

    if len(words) < 2:
        return sentence

    words[0], words[-1] = words[-1], words[0]

    swapped_sentence = ' '.join(words)
    return swapped_sentence


sentence = "мама мыла раму"
result = swap_first_last_word(sentence)
print("Предложение с поменянными местами первым и последним словом:", result)
