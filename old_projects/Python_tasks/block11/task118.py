years = [
    1980, 1975, 1990, 1985, 1970,
    1980, 1975, 1992, 1988, 1973,
    1980, 1975, 1990, 1985, 1970,
    1980, 1975, 1992, 1988, 1973,
    1980, 1975, 1990, 1985, 1970,
    1980, 1975, 1992
]

min_year = min(years)

indices = [i for i, year in enumerate(years) if year == min_year]

first_index = indices[0] + 1

last_index = indices[-1] + 1

print(f"номер самого старшего (первый случай): {first_index}")
print(f"номер самого старшего(последний случай): {last_index}")
