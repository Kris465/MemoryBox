n_workers = 12
n_months = 3
workers_salary = []

for worker_id in range(1, n_workers + 1):
    print(f"Введите зарплату работника {worker_id} за три месяца через пробел")
    row = list(map(float, input().split()))
    workers_salary.append(row)

max_salary = max(max(row) for row in workers_salary)
print(f"Максимальная зарплата из таблицы: {max_salary:.2f}")

quarterly_sums = [sum(row) for row in workers_salary]
max_worker_index = quarterly_sums.index(max(quarterly_sums)) + 1
print(f"Работник под номером {max_worker_index} получил наибольшую сумму.")

monthly_totals = [sum([row[i] for row in workers_salary])
                  for i in range(n_months)]
max_month_index = monthly_totals.index(max(monthly_totals)) + 1
print(f"Наибольшая общая зарплата всех работников была в месяце \
    {max_month_index}.")
