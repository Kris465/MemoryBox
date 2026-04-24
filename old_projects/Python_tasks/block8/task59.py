def generate_fractions(limit):
    fractions = set()
    for denominator in range(2, limit + 1):
        for numerator in range(1, denominator):
            fractions.add((numerator, denominator))
    return fractions


fractions = generate_fractions(7)
for fraction in fractions:
    print(f"{fraction[0]}/{fraction[1]}")
