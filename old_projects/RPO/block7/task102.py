def side_with_more_residents(houses):
    even_side = 0
    odd_side = 0
    houses = [10, 20, 30, 40, 50]

    for residents in houses:
        if len(houses) % 2 == 1:

            if houses.index(residents) < len(houses) // 2 + 1:
                odd_side += residents
            else:
                even_side += residents
        else:
            if houses.index(residents) <= len(houses) // 2:
                odd_side += residents
            else:
                even_side += residents

    return "нечётная сторона" if odd_side > even_side else "чётная сторона"


print(side_with_more_residents(houses))
