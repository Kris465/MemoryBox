def computer_expression(n):
    result = n**2
    for i in range(n-1, 0, -1):
        result = (result - i**2)**2
    return result

# Пример для n = 5
print(computer_expression(5))

