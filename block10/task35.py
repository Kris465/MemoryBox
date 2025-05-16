def find_numbers(start=500, limit=20):
    found_count = 0
    current = start
    result = []
    while found_count < limit:
        if current % 13 == 0 or current % 17 == 0:
            result.append(current)
            found_count += 1
        current += 1

    return result


print(find_numbers())
