import datetime

a = datetime.date(year=2000, month=1, day=1)
b = datetime.date(year=2024, month=2, day=28)
print(int((b - a).days / (365.2425)))
