heights = [-170, 160, -180, 155, -175, 165]

boys_heights = [height for height in heights if height < 0]
girls_heights = [height for height in heights if height >= 0]

if len(boys_heights) > 0 and len(girls_heights) > 0:
    avg_boy_height = abs(sum(boys_heights)) / len(boys_heights)
    avg_girl_height = sum(girls_heights) / len(girls_heights)
    if avg_boy_height > avg_girl_height + 10:
        print("Средний рост мальчиков превышает средний рост девочек\
            более чем на 10 см.")
    else:
        print("Средний рост мальчиков не превышает средний рост девочек\
              более чем на 10 см.")
else:
    print("Недостаточно данных для расчета.")
