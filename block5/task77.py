def sum_series(n):
    series = [-1]
    term = 2
    for i in range(1, n+1):
        series.append(-1 / term)
        term *= 2
    return sum(series)


print(sum_series(10))
