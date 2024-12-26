A = True
B = False
C = False

# a) не A и B
result_a = not A and B
print(f"a) {result_a}")

# b) A или не B
result_b = A or not B
print(f"b) {result_b}")

# в) A и B или C
result_c = (A and B) or C
print(f"в) {result_c}")
