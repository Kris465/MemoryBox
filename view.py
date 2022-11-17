# Здесь интерфейс

def get_value():
    print("Hello! Welcome to our caculator.")
    
    while True:
        inp = input("Input you operation. Please separate numbers from the sign of operation with space: ")
        try_act = inp
        data = try_act.split()

        if len(data) == 3:
            if data[1] == "+" or data[2] == "-" or data[1] == "*" or data[1] == "/":
                print("Thank you!")
                break
        else:
            print("Your input is incorrect. Try again, please.")

    return inp


def output(result):
    if result % 10 == 0:
        print(f"Your result is:", int(result))
    elif isinstance(result, float):
        print(f"Your result is:", result)
    else: print(result)
