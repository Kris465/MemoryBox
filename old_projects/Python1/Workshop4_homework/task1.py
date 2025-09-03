# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

def round_func():
    number = float(input("Input your number, please: "))
    fractional_part = float(input("Input the sample of your number: "))
    current = 0

    while fractional_part != int(fractional_part):
        fractional_part *= 10
        current += 1

    number = round(number, current)
    temp = round(number - int(number), current)
    length_frac = len(str(temp)) - 2
    
    if length_frac < current:
        print(str(number) + "0" * (current - length_frac))
    else: 
        print(f"Your number in asked sample: {number}")

round_func()
