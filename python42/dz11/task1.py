n = int(input('Введите количество строк: '))

# квадратик
# print(*[''.join([' * ' for i in range(n)]) + '\n' for j in range(n)], end='')

# треугольник, левый нижний угол
# print(*[''.join([' * ' for i in range(i + 1)]) + '\n' for i in range(n)], end='')

# for i in range(n):
#     for j in range(n):
#         if j <= i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# треугольник, правый верхний угол

# print(*[''.join([' * ' if j>=i else '   ' for j in range(n)]) + '\n' for i in range(n)], end='')

# for i in range(n):
#     for j in range(n):
#         if j >= i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# Не то, но штука прикольная получилась
# print(*[''.join([' * ' if i == j or i + j == n - 1 else '   ' for j in range(n)]) + '\n' for i in range(n)], end='')

# правый нижний угол

# for i in range(n):
#     for j in range(n):
#         if j >= n - 1 - i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# левый верхний угол

# for i in range(n):
#     for j in range(n):
#         if j <= i:
#             print(' ', end=' ')
#         else:
#             print('*', end=' ')
#     print()

