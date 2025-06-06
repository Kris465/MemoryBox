heights = [190, 185, 180, 175, 170, 165, 160,
           155, 150, 145, 140, 135, 130, 125, 120]
h = 168

place = sum(x > h for x in heights) + 1
print(place)
