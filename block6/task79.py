import math


def is_member_of_geometric_progression(m, g, z):
    if g == 0:
        return m == 0
    elif m == 0:
        return False
    elif abs(z) < 1:
        return False
    else:
        try:
            exponent = math.log(m / g, z)
            return exponent.is_integer()
        except ValueError:
            return False


m = 24
g = 3
z = 2
print(is_member_of_geometric_progression(m, g, z))
