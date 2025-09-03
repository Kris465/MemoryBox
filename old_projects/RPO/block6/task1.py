def process_sequence():
    total_sum = 0     
    count = 0         

    while True:       
        num = int(input('Введите число (чтобы выйти из цикла напишите 0): '))   
        if num == 0:         
            break
        total_sum += num     
        count += 1           

    return total_sum, count  

sum_result, count_result = process_sequence()
print(f"Сумма всех чисел последовательности: {sum_result}")
print(f"Количество всех чисел последовательности: {count_result}")