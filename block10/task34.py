def find_numbers(divisor=19, start=100, count=15):

    first_number = ((start + divisor - 1) // divisor) * divisor

    result = [first_number + i*divisor for i in range(count)]
    return result


result = find_numbers()
print(result)
