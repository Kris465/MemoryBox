s = 5
print(f"a) s = {s}, тип: {type(s)}")
s = 57
print(f"a) s = {s}, тип: {type(s)}")

s = 6
print(f"б) s = {s}, тип: {type(s)}")
s = -5.2 * s
print(f"б) s = {s}, тип: {type(s)}")
s = 0
print(f"б) s = {s}, тип: {type(s)}")

try:
    s = -5.2 * s
except NameError as e:
    print(e)
print("Hello")
