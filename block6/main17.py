summ = 1
index = 2.
n = int(input('--> '))
 
while summ + 1 / index < n:
    summ += 1 / index
    index += 1
print(summ)
