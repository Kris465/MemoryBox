a = int(input("Введите число а: "))
b = int(input("Введите число b: "))


# def nod(a, b):
   #  if a == 0 or b == 0:
     #    return max(a, b)
   #  else:
       #  if a > b:
          #   return nod(a - b, b)
      #   else:
         #    return nod(a, b - a)


def nodd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return max(a, b)


print(nodd(a, b))
