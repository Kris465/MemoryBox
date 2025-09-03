sum_value = 0
current_term = 1


for i in range(9):
    sum_value += current_term
    current_term /= 3
    
    
    print("Сумма ряда:", sum_value)
