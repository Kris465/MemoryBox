p = [1200, 300, 400, 500]
s = [80, 100, 103, 115]
print(sum([x/y for x, y in zip(p, s)])/len(p))
