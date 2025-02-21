def product_sum(n, array):
    result = 1
    for i in range(1, n+1):
        result *= array[i-1]
    return result


n = int(input("Введите натуральное число n: "))
array = list(map(int, input("Введите массив чисел через пробел: ").split()))
print("Сумма произведения элементов массива:", product_sum(n, array))
