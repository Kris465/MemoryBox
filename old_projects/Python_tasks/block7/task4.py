def sum_of_multiples_of_four(a, b):
    start = ((a + 3) // 4) * 4
    end = (b // 4) * 4
    if start > end:
        return 0
    return 4 * (start // 4 + end // 4) * (end // 4 - start // 4 + 1) // 2
