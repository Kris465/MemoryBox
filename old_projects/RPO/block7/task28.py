def main():


    n = int(input())
    a = list(map(int, input().split()))

    p = int(input())
    k = int(input())

    result_a = count_greater_than_p(a, p)
    print("Количество чисел, больших p:", result_a)

    result_b = count_numbers_ending_with_5(a)
    print("Количество чисел, оканчивающихся на 5:", result_b)

    result_c = count_multiples_of_k(a, k)
    print("Количество чисел, кратных k:", result_c)


main()
