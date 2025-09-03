def find_multiples(n1, n2, start, count):
    multiples = []
    num = start + 1

    while len(multiples) < count:
        if num % n1 == 0 or num % n2 == 0:
            multiples.append(num)
        num += 1

    return multiples


result = find_multiples(13, 17, 500, 20)
print(result)
