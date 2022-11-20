# Здесь интерфейс

def get_value():
    print("Hello! Welcome to our caculator.")
    expression = input("Input your expression, please: ")
    kind_operation = input("For complex numbers input 1, for usual numbers input 2: ")

    if kind_operation == 1:
        reel_part = input("Input the reel or main part of the first complex number: ")
        imaginaire_part = input("Input the imaginaire part of the first complex number: ")
        sign = input("Input the sing of operation: ")
        reel_part1 = input("Input the reel or main part of the second complex number: ")
        imaginaire_part1 = input("Input the imaginaire part of the second complex number: ")
        step = [reel_part + imaginaire_part, sign, reel_part1 + imaginaire_part1]
    else:
        data = expression.split()



    # kind_operation = input("For complex numbers input 1, for usual numbers input 2: ")
    # if kind_operation == 1:
    #     reel_part = input("Input the reel or main part of the first complex number: ")
    #     imaginaire_part = input("Input the imaginaire part of the first complex number: ")
    #     sign = input("Input the sing of operation: ")
    #     reel_part1 = input("Input the reel or main part of the second complex number: ")
    #     imaginaire_part1 = input("Input the imaginaire part of the second complex number: ")
    #     step = [reel_part + imaginaire_part, sign, reel_part1 + imaginaire_part1]
    # else:
    #     flag = True
    #     while flag == True:
    #         checked_lst = []
    #         user_str = input("Input your expression: ")
    #         model_lst = ["+", "-", "/", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "(", ")"]
    #         for i in user_str:
    #             if i in model_lst:
    #                 checked_lst.append(i)
    #                 flag = False
    #             else:
    #                 print("Yout input is incorrect. Try again, please.")
    #                 user_str = input("Input your expression: ")
    #                 flag = True
                

    # print(step)
    
    # while True:
    #     inp = input("Input you operation. Please separate numbers from the sign of operation with space: ")
    #     try_act = inp
    #     data = try_act.split()

    #     if len(data) == 3:
    #         if data[1] == "+" or data[1] == "-" or data[1] == "*" or data[1] == "/":
    #             print("Thank you!")
    #             break

    #     print("Your input is incorrect. Try again, please.")

    return step, kind_operation


def output(result):
    try:
        if result.is_integer():
            print(f"Your result is:", int(result))
        elif isinstance(result, float):
            print(f"Your result is:", result)
        else: print(result)
    except:
        print(result)

get_value()