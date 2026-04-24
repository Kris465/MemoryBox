a = int(input())
b = int(input())

divisible_a_b = int(a % b == 0)
divisible_b_a = int(b % a == 0)

result = max(divisible_a_b, divisible_b_a)

print(result)
