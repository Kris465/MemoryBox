#a)
s = 14
print(s)

k = -3 

try:
    s = 2 * s
    print(s + k)
    print(s + k)
except NameError as e:
    print(e)

d = s + 1
print(d)

try:
    d = s + 1
    print(d + s)
    print(d + s)
except NameError as e:
    print(e)
    
s = d
print(s)

try:
    s = d + s
    print(d + s)
    print(d + s)
except NameError as e:
    print(e)

k = 2 * s 
print(k)

try:
    k = 2 * s
    print(k)
except NameError as e:
    print(e)
    
#б)
s = 0
print(s)

k = 30
print(k)

try:
    s + k
    print(s + k)
    print(s + k)
except NameError as e:
    print(e)
    

d = k - 5
print(d)

try:
    d + k
    print(d + k)
    print(d + k)
except NameError as e:
    print(e)
    
    
k = 2 * b 
print(k)

try:
    k = 2 * b 
    print(k)
except NameError as e:
    print(e)
    
    
s = k - 100
print(s)

try:
    s = k - 100
    print(s)
except NameError as e:
    print(e)
    
    