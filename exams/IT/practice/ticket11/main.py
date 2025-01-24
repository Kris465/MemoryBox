def fizma_table(A, B, C, logic_operation):
    print(f"{A}, {B}, {C}, result")
    print("-" * 20)
    
    for A  in (A, not A):
        for B in (B, not B):
            for C in (C, not C):
                match logic_operation:
                    case 'AND':
                        result = A and B and C
                        return result
                    case 'OR':
                        result = A or B or C
                        return result
                    case 'NAND':
                        result = not (A and B and C)
                        return result
                    case 'NOR':
                        result = not (A or B or C)
                        return result
                    case 'XOR':
                        result = A ^ B ^ C
                        return result
                    case 'XNOR':
                        result = not (A ^ B ^ C)
                        return result
                    case _:
                        return 'Этой функции не существует'
    print(f"{A}, {B}, {C}, result")

A = input("Введите False или True: ")
B = input("Введите False или True: ")
C = input("Введите False или True: ")
logic_operation = input("Введите AND/OR/NAND/NOR/XOR/XNOR): ").upper()
x = 0
while x < 6:
    x += 1
    result = fizma_table(A, B, C, logic_operation)
    print(result)
