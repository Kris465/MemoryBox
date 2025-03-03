def find_kth_digit(k):

    number_index = (k - 1) // 3 + 101

    if k % 3 == 1:

        digit = number_index // 100
    elif k % 3 == 2:

        digit = (number_index // 10) % 10
    else:

        digit = number_index % 10

    return digit


for k in range(1, 151):
    print(f"Кратное трём: {find_kth_digit(k)}" if k % 3 == 0 else f"1, 4, 7, \
          {find_kth_digit(k)}" if k % 3 == 1 else f"2, 5, 8, ...:\
              {find_kth_digit(k)}")
