# Здесь интерфейс

def get_value():
    inp = input("Input you operation. Please separate numbers from the sign of operation with space: ")
    try_act = inp
    data = try_act.split()
    if str(data[0]).isdigit() and str(data[2]).isdigit():
        if data[1] == "+" or data[1] == "-" or data[1] == "/" or data[1] == "*":
            return inp
        else: 
            print("Yout input is incorrect. Try again, please.")
            get_value()
    else: print("...")


def output(result):
    if str(result).isdigit():
        print(f"Your result is:", *result)
    else: print(result)
