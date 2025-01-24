def main():
    first_operand = input("Введите первое логичское значение (True/False): ")
    second_operand = input("Введите второе логическое значение (True/False): ")
    
    if first_operand.lower() == 'true':
        first_operand = True
    else:
        first_operand = False
    if second_operand.lower() == 'true':
        second_operand = True
    else:
        second_operand = False
    

    and_result = first_operand and second_operand
    or_result = first_operand or second_operand
    not_first_result = not first_operand
    not_second_result = not second_operand

    print(f"Результат AND: {and_result}")
    print(f"Результат OR: {or_result}")
    print(f"Результат NOT первого операнда: {not_first_result}")
    print(f"Результат NOT второго опернда: {not_second_result}")


main()
