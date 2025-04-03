import random
import time


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")


def interactive_search(root, key):
    steps = []
    start_time = time.time()
    current = root
    while current is not None:
        steps.append(f"Нода: {current.val}")
        if key == current.val:
            steps.append(f"Найдено значение {key}! Поздравляю!")
            break
        elif key < current.val:
            steps.append(f"{key} < {current.val} — идём влево")
            current = current.left
        else:
            steps.append(f"{key} > {current.val} — идём вправо")
            current = current.right
    end_time = time.time()
    return steps, end_time - start_time


# Генерация случайного дерева
random.seed(42)
values = random.sample(range(1, 100), 15)  # 15 уникальных чисел от 1 до 100
root = None
for v in values:
    root = insert(root, v)

# Вывод дерева
print("\nСгенерированное дерево:")
print_tree(root)

# Ввод пользователя
target = int(input("\nВведите число для поиска: "))

# Поиск с выводом шагов
steps, time_taken = interactive_search(root, target)
print("\nПроцесс поиска:")
print("\n".join(steps))
print(f"\nПоиск занял {time_taken:.6f} секунд.")
