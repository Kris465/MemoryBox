def generate_sequencef(initial_value, step_size, number_of_steps):
    sequence = [initial_value]
    current_value = initial_value
    for _ in range(number_of_steps):
        current_value += step_size
        sequence.append(current_value)
    return sequence


initial_value = 1
step_size = 1.5
number_of_steps = 5
result = generate_sequencef(initial_value, step_size, number_of_steps)
print("Последовательность из {} чисел: {}".format(number_of_steps, result))
