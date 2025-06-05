def remove_by_values(heights, h1, h2):
    new_heights = []
    removed_h1 = False
    removed_h2 = False

    for h in heights:
        if not removed_h1 and h == h1:
            removed_h1 = True
        elif not removed_h2 and h == h2:
            removed_h2 = True
        else:
            new_heights.append(h)
    return new_heights


heights = [190, 185, 183, 180, 178, 175, 173, 170, 168, 165, 163, 160, 158,
           155, 153, 150, 148, 145, 143, 140, 138, 135, 133, 130, 128]
h1, h2 = 183, 175
result = remove_by_values(heights, h1, h2)
print(result)
