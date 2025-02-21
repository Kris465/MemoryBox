def find_nth_term(k):
    numerators = [1, 2]
    denominators = [1, 1]

    for _ in range(2, k):
        new_numerator = numerators[-1] + numerators[-2]
        new_denominator = denominators[-1] + denominators[-2]
        numerators.append(new_numerator)
        denominators.append(new_denominator)

    return numerators[-1] / denominators[-1]


k = 5
result = find_nth_term(k)
print("k-й член последовательности: {}".format(result))
