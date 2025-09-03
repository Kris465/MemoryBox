salary_data = [
    [1000, 1100, 1200],
    [2000, 2100, 2200],
    [3000, 3100, 3200],
    [4000, 4100, 4200],
    [5000, 5100, 5200],
    [6000, 6100, 6200],
    [7000, 7100, 7200],
    [8000, 8100, 8200],
    [9000, 9100, 9200],
    [10000, 10100, 10200],
    [11000, 11100, 11200],
    [12000, 12100, 12200]
]


def calculate_total_quarterly(salary_data):
    return sum(sum(monthly_salary) for monthly_salary in salary_data)


def calculate_quarterly_per_employee(salary_data):
    return [sum(employee_monthly_salary) for employee_monthly_salary
            in salary_data]


def calculate_monthly_total(salary_data):
    return [sum([employee_monthly_salary[i] for employee_monthly_salary
                 in salary_data])
            for i in range(len(salary_data[0]))]


if __name__ == "__main__":
    total_salary_quarterly = calculate_total_quarterly(salary_data)
    print("Общая сумма, выплаченная за квартал:", total_salary_quarterly)

    quarterly_per_employee = calculate_quarterly_per_employee(salary_data)
    print("Зарплата каждого работника за квартал:")
    for i, salary in enumerate(quarterly_per_employee):
        print(f"Работник {i + 1}: {salary}")

    monthly_total = calculate_monthly_total(salary_data)
    print("Общая зарплата всех работников за каждый месяц:")
    for i, month_salary in enumerate(monthly_total):
        print(f"Месяц {i + 1}: {month_salary}")
