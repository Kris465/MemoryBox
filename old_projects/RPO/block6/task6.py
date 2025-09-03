def analyze_sequence(seq, n):
    
    sum_less = sum(x for x in seq if x < n)
    lower, upper, l_val, u_val = next(
        (i, i + 1, seq[i], seq[i + 1])
        for i, x in enumerate(seq)
        if x < n < seq[i + 1]
    )
    
    return sum_less, (lower + 1, upper + 1, l_val, u_val)


seq = [1.0, 2.5, 3.7, 4.8, 6.2, 7.5, 8.9, 10.1, 
       11.3, 12.6, 13.8, 15.0, 16.2, 17.5, 18.9]
n = 9.5

sum_result, (l_idx, u_idx, l_val, u_val) = analyze_sequence(seq, n)

print(f"Сумма чисел, меньших {n}: {sum_result}")
print(f"n между элементами {l_idx} (i_val) и {u_idx} (u_val)")
