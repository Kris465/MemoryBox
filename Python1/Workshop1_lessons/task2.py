# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

def max_num():
    m_number = 0
    for i in range(5):
        number = int(input("Input your number: "))
        if m_number < number:
            m_number = number
    
    print(m_number)

max_num()
