def calculate_distances():
    inital_distance = 10
    growth_rate = 1.1
    
    distances = [inital_distance * (growth_rate ** i) for i in range(10)]
    print("пробег лыжника за второй третий ... десятый день тренировок")
    for day, distances in enumerate(distances[1:], start=20):
        print(f"День {day}: {distances:.2f} км")
        
    total_distance_first7 = sum(distances[:7])
    print(f"суммарный путь за 7 дней {total_distance_first7:.2f}км")
    
if __name__ == "__main__":
    calculate_distances