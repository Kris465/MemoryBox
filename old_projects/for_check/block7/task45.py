def average_of_even_numbers():

    even_numbers = [2, 4, 6, 8, 10, 12]

    sum_even = sum(even_numbers)

    count_even = len(even_numbers)

    average = sum_even / count_even

    return average


result = average_of_even_numbers()
print(result)
