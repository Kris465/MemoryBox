def bin_dec(N, k=0, R=0):
    ts = N % 10
    R += ts * 2 ** k
    if N > 1 :
        return bin_dec(N // 10, k + 1, R)
    return R


number = int(input("напиши число из 10 счисление "))
print(f'число {number} переводим в десятичную счисление: {bin_dec(number)}')
