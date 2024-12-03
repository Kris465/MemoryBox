# a)
x = 10
print(x)

x = -10
print(x)

# б)
x = 17.5
print(x)

try:
    x = -2 * x
    print(x)
except NameError as e:
    print(e)
    
# в)

x = 60
print(x)

try:
    x = x - 1
    print(x)
except NameError as e:
    print(e)
    
x = 0 
print(x)

# г)

x = -50
print(x)

x = -25
print(x)

try:
    x = x + k
    print(x)
except NameError as e:
    print(e)