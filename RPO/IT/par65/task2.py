import random


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return steps


def average_steps_binary_search(num_trials=1000):
    total_steps = 0

    for _ in range(num_trials):
        arr = random.sample(range(101), 32)
        arr.sort()
        target = random.choice(arr)

        steps = binary_search(arr, target)
        total_steps += steps

    average_steps = total_steps / num_trials
    return average_steps


average = average_steps_binary_search()
print(f"Среднее число шагов при двоичном поиске: {average:.2f}")
