X = False
Y = False
Z = True

res_a = X or Y and not Z
res_b = not X and not Y
res_c = X and (not Y or Z)
res_d = X and (not Y or Z)
res_e = not (X and Z) or Y
res_f = X or not (Y or Z)


print("а) X или Y и не Z =", res_a)
print("б) не X и не Y =", res_b)
print("в) X и не Y или Z =", res_c)
print("г) X и не Y или Z =", res_d)
print("д) не (X и Z) или Y =", res_e)
print("е) X или не (Y или Z) =", res_f)
