#Солончекно Кирилл 

def digit_sum(n):
    return sum(int(digit)) for digit in str(n)


def find_spicial_numbers(n):
    special_numbers = []
    for i in range(N + 1):
        original_sum = digit_sum(i)
        if all(original_sum == digit_sum(i * multiplier) for multiplier in  range(2, 10)):
            special_numbers.append(i)
        return special_numbers
    
N = int(input("Введите число N: "))
special_numbers = find_spicial_numbers(N)

print("Число с неизменной суммой цифр:", special_numbers)



