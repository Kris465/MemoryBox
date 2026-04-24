def find_numbers():
    count = 0
    number = 107

    while count < 10:
        if number % 9 == 0 and str(number).endswith('7'):
            print(number)
            count += 1
        number += 18

find_numbers()
