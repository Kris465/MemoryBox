def main():
    user_input=input("Введите что-то: ")
   
    try:
       float_value = float(user_input)
       if '.' in user_input or 'e' in user_input.lower():
           print(f"Тип: {type(float_value).__name__}(число с плавающей запятой)")
       else:
           print(f"Тип:{type(int(float_value)).__name__}(целое число)")
    except ValueError:
        if user_input.lower() in ['true', 'false']:
            print(f"Тип:{type(user_input.lower() == 'true').__name__}(логическое значение)")
        else:
            print(f"Тип: {type(user_input).__name__}")
            


main()
