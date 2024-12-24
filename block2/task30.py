n = 456
first_digit = n // 100   
last_two_digits = n % 100 
for x in range(100, 1000):
    hundreds = x // 100       
    tens = (x // 10) % 10      
    units = x % 10            
    if tens == first_digit and (hundreds * 10 + units) == last_two_digits:
        print(f"Найденное трехзначное число x: {x}")
        break
