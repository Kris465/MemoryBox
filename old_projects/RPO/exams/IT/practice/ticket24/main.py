import numpy as np


def generate_random_matrix(size=3):
    return np.random.randint(0, 10, size=(size, size))


def transpose(matrix):
    return matrix.T


def process_elements(matrix):
    processed_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if element % 2 == 0:
                new_row.append(element**2)
            else:
                new_row.append(element**3)
        processed_matrix.append(new_row)
    return np.array(processed_matrix)


def main():
    matrix1 = generate_random_matrix()
    matrix2 = generate_random_matrix()

    transposed_matrix1 = transpose(matrix1)
    transposed_matrix2 = transpose(matrix2)

    processed_transposed_matrix1 = process_elements(transposed_matrix1)
    processed_transposed_matrix2 = process_elements(transposed_matrix2)

    print("\nМатрица 1:")
    print(matrix1)
    print("\nТранспонированная матрица 1:")
    print(transposed_matrix1)
    print("\nОбработанная транспонированная матрица 1:")
    print(processed_transposed_matrix1)

    print("\n\nМатрица 2:")
    print(matrix2)
    print("\nТранспонированная матрица 2:")
    print(transposed_matrix2)
    print("\nОбработанная транспонированная матрица 2:")
    print(processed_transposed_matrix2)


if __name__ == "__main__":
    main()
