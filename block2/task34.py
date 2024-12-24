def decompose_sum(a2, a1, b):
  if not (0 <= a2 <= 9 and 0 <= a1 <= 9 and 0 <= b <= 9):
    return None, None

  sum_num = a2 * 10 + a1 + b
  tens = sum_num // 10
  units = sum_num % 10

  return tens, units

tens_digit, units_digit = decompose_sum(2, 5, 7)  

if tens_digit is not None:
  print(f"Tens digit: {tens_digit}, Units digit: {units_digit}")
else:
  print("Invalid input")


tens_digit, units_digit = decompose_sum(9,9,9) 

if tens_digit is not None:
  print(f"Tens digit: {tens_digit}, Units digit: {units_digit}")
else:
  print("Invalid input")


tens_digit, units_digit = decompose_sum(10,5,2) 

if tens_digit is not None:
  print(f"Tens digit: {tens_digit}, Units digit: {units_digit}")
else:
  print("Invalid input")
