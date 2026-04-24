marks = [4, 4, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4]


def has_threes(marks):
    for mark in marks:
        if mark == 3:
            return True
    return False


if has_threes(marks):
    print("Среди оценок есть тройки!")
else:
    print("Среди оценок нет троек!)")
