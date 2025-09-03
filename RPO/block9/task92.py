sentence = "Дано предложение."

modified_sentence = ''.join('ы' if i % 2 == 0 else char for i,
                            char in enumerate(sentence))


print(modified_sentence)
