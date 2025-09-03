array = [3, 5, 7, 2, 5, 9, 5, 5, 5, 9, 4]

for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            count += 1
    if count == 2:
        print("Есть элемент, встречающийся ровно два раза.")
        break
else:
    print("Нет элементов, встречающихся ровно два раза.")
