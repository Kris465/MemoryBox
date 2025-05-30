mountain_names = ["Аконкагуа", "Денали", "Эверест", "Килиманджаро"]
mountain_heights = [6962, 6190, 8848, 5895]
new_peak_name = "Монблан"
new_peak_height = 4808


def insert_mountain_peak(heights, new_height, new_name, names):
    insert_pos = 0
    while insert_pos < len(names) and names[insert_pos] < new_name:
        insert_pos += 1
    # Вставляем новую высоту
    heights.insert(insert_pos, new_height)
    return heights
