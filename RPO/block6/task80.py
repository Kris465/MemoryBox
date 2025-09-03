def most_frequent_digit(n):
    return '0' if str(n).count('0') > str(n).count('9') else '9'


n = 1090
print(most_frequent_digit(n))
