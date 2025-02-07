from random import randint

def triple_characters(s):
    """Утроить каждый символ в строке."""
    return ''.join([char * 3 for char in s])

def simulate_transmission(tripled_string):
    """Имитация передачи сообщения с случайными удалениями символов."""
    transmitted_message = []
    i = 0
    
    while i < len(tripled_string):
        segment = tripled_string[i:i + 4]
        
        if len(segment) == 4:
            k = randint(0, 2)
            if k == 0:
                transmitted_message.append(segment[:-1])
            elif k == 1:
                transmitted_message.append(segment[1:])
            else:
                transmitted_message.append(segment[0:2] + segment[3:])
        else:
            transmitted_message.append(segment)

        i += 4

    return ''.join(transmitted_message)

def remove_duplicates(s):
    """Удалить дублирующиеся символы из строки."""
    return ''.join([s[i] for i in range(len(s) - 1) if s[i] != s[i + 1]]) + s[-1]

def main():
    original_string = input('Введите ваше сообщение: ')
    tripled_string = triple_characters(original_string)
    
    print(f"Утроенное сообщение: {tripled_string}")
    
    redflag = simulate_transmission(tripled_string)
    print(f"Полученное сообщение с помехами: {redflag}")
    
    greenflag = remove_duplicates(redflag)
    print(f"Сообщение без дубликатов: {greenflag}")


if __name__ == "__main__":
    main()
