# Здесь интерфейс

def view(data):
    print(data)

def get_value():
    return input("Input you operation. Please separate numbers from the sign of operation with space: ") # число пробел знак пробел число

def output(result):
    if str(result).isdigit():
        print(f"Your result is:", *result)
    elif result % 10 != 0:
        print(f"Yout result is:", round(result, 2))
    else: print(result)
