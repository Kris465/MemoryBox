def check_ji_shi(sequence):
    incorrect_pairs = {'же', 'жа', 'эж', 'шо', 'ше', 'ша'}

    words = sequence.split() if isinstance(sequence, str) else sequence

    for word in words:
        for i in range(len(word) - 1):
            current_pair = word[i:i + 2].lower()
            if current_pair in incorrect_pairs:
                print(f"Ошибка! В слове '{word}'неверная запись сочетания\
                    '{current_pair}'.")
                return False
    print("Все слова содержат верные сочетания.")
    return True


test_sequence = "Жили были мыши жирненькие"
check_ji_shi(test_sequence)

wrong_sequence = "Жило было животное желтое"
check_ji_shi(wrong_sequence)
