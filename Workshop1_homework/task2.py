# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def truth_predicate():
#     lst = []

#     for i in range(3):
#         lst.append(int(input("Input 0 or 1: ")))

#     left = not (lst[0] or lst[1] or lst[2])
#     right = not lst[0] and not lst[1] and not lst[2]
#     if left == right:
#         print("True")
#     else: print("False")

# truth_predicate()

flag = True
for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            left = not(x or y or z)
            right = not(x) and not(y) and not(z)
            print(x, y, z, left == right)
            if left != right:
                flag = False
if flag == True:
    print("True")
else: 
    print("False")