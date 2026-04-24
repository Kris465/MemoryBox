def find_numbers():
    start_num = 107
    result = []

    while len(result) < 10:
        for i in range(start_num, start_num+90):
            if i % 9 == 0 and str(i)[-1] == '7':
                result.append(i)

        start_num += 90

    return result


numbers = find_numbers()
print(numbers)
