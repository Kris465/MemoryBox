def nth_term_arithmetic_progression(a1, d, n):
    if n == 1:
        return a1
    else:
        return nth_term_arithmetic_progression(a1, d, n - 1) + d


first_term = 2
common_difference = 3
term_number = 5

nth_term = nth_term_arithmetic_progression(
    first_term, common_difference, term_number)
print(f"{term_number}-й член арифметической прогрессии: {nth_term}")


def arithmetic_progression_sum(a1, d, n):
    if n == 1:
        return a1
    else:
        current_term = nth_term_arithmetic_progression(a1, d, n)
        previous_sum = arithmetic_progression_sum(a1, d, n - 1)
        return previous_sum + current_term


first_term = 2
common_difference = 3
number_of_terms = 5

progression_sum = arithmetic_progression_sum(
    first_term, common_difference, number_of_terms)
print(f"Сумма первых {number_of_terms} членов арифметической прогрессии: {
    progression_sum}")
