a, b, c, d, e, f = map(int, input().split())

# Условие, что фигура на (a, b) может ходить на (e, f)
# без попадания под удар фигуры на (c, d)

# а) ладья и ладья
cond_a = (a == e or b == f) and not (c == e or d == f)

# б) ладья и ферзь
cond_b = ((a == e or b == f) or (abs(a - e) == abs(b - f))) and not (c == e or d == f)

# в) ладья и конь
cond_v = ((a == e or b == f) or (abs(a - e) == abs(b - f))) and not (c == e or d == f)

# г) ладья и слон
cond_g = ((a == e or b == f) or (abs(a - e) == abs(b - f))) and not (c == e or d == f)

# д) ферзь и ферзь
cond_d = (((a == e or b == f) or (abs(a - e) == abs(b - f)))) and not (c == e and d == f)

# е) ферзь и ладья
cond_e = (((a == e or b == f) or (abs(a - e) == abs(b - f)))) and not (c == e and d == f)

# ж) ферзь и конь
cond_zh = (((abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2))) and not (c == e and d == f)

# з) ферзь и слон
cond_z = (((abs(a - e) == abs(b - f)))) and not (c == e and d == f)

# и) конь и конь
cond_i = ((abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2)) and not (c == e and d == f)

# к) конь и ладья
cond_k = ((abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2)) and not (c == e or d == f)

# л) конь и ферзь
cond_l = ((abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2) or
          (a == e or b == f) or (abs(a - e) == abs(b - f))) and not (c == e and d == f)

# м) конь и слон
cond_m = ((abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2) or
          (abs(a - e) == abs(b - f))) and not (c == e and d == f)

# н) слон и слон
cond_n = (abs(a - e) == abs(b - f)) and not (c == e and d == f)

# о) слон и ферзь
cond_o = ((abs(a - e) == abs(b - f)) or (a == e or b == f)) and not (c == e and d == f)

# п) слон и конь
cond_p = ((abs(a - e) == abs(b - f)) or (abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2)) and not (c == e and d == f)

# р) слон и ладья
cond_r = ((abs(a - e) == abs(b - f)) or (a == e or b == f)) and not (c == e or d == f)

# с) король и слон
cond_s = (max(abs(a - e), abs(b - f)) == 1) and not (c == e and d == f)

# т) король и ферзь
cond_t = (max(abs(a - e), abs(b - f)) <= 1) and not (c == e and d == f)

# у) король и конь
cond_u = ((abs(a - e) == 1 and abs(b - f) == 0) or (abs(a - e) == 0 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 1)) and not (c == e and d == f)

# ф) король и ладья
cond_f = (max(abs(a - e), abs(b - f)) == 1) and not (c == e and d == f)

# вывод
print(
    cond_a, cond_b, cond_v, cond_g, cond_d, cond_e, cond_zh, cond_z, cond_i, cond_k,
    cond_l, cond_m, cond_n, cond_o, cond_p, cond_r, cond_s, cond_t, cond_u, cond_f
)