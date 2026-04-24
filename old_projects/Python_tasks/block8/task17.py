salaries = [
    [30000, 32000, 31000],
    [35000, 34000, 36000],
    [40000, 41000, 42000],
    [25000, 26000, 27000],
    [50000, 52000, 51000],
    [30000, 31000, 32000],
    [35000, 36000, 37000],
    [40000, 42000, 41000],
    [25000, 27000, 26000],
    [50000, 51000, 52000],
    [30000, 32000, 31000],
    [35000, 34000, 36000]
]


best_month_per_worker = [
    row.index(max(row)) + 1 for row in salaries
]


best_worker_per_month = [
    monthly.index(max(monthly)) + 1 for monthly in zip(*salaries)
]


print("а) Лучший месяц для каждого работника:", best_month_per_worker)
print("б) Лучший работник в каждом месяце:", best_worker_per_month)
