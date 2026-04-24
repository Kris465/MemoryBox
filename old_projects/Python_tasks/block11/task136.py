birth_years = [1985, 1990, 1978, 1982, 1975, 1995, 1980, 1970, 1988, 1973,
               1992, 1984, 1976, 1981, 1979, 1993, 1983, 1974, 1986, 1972,
               1991, 1987, 1971, 1989, 1994, 1985, 1977, 1980, 1978]

oldest_year = float('inf')
second_oldest_year = float('inf')

for year in birth_years:
    if year < oldest_year:
        second_oldest_year = oldest_year
        oldest_year = year
    elif oldest_year < year < second_oldest_year:
        second_oldest_year = year

print("Годы рождения двух самых старых:", oldest_year, second_oldest_year)
