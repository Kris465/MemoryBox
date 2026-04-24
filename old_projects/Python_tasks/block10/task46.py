def geometric_progression_nth_term(b1, q, n):
    if n == 1:
        return b1
    else:
        return geometric_progression_nth_term(b1, q, n - 1) * q


first_term = 2
common_ratio = 3
term_number = 5

nth_term = geometric_progression_nth_term(first_term,
                                          common_ratio, term_number)
print(f"{term_number}-й член геометрической прогрессии: {nth_term}")


def geometric_progression_sum(b1, q, n):
    if n == 1:
        return b1
    else:
        current_term = geometric_progression_nth_term(b1, q, n)
        previous_sum = geometric_progression_sum(b1, q, n - 1)
        return previous_sum + current_term


first_term = 2
common_ratio = 3
number_of_terms = 5

progression_sum = geometric_progression_sum(first_term, common_ratio,
                                            number_of_terms)
print(f"Сумма первых {number_of_terms} членов геометрической \
    прогрессии: {progression_sum}")
