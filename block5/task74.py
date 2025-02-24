import math

inner_diameter_first_ball_cm = 10.0  
wall_thickness_cm = 0.5              
number_of_balls = 12

def calculate_total_volume(inner_diameter_first_ball_cm, wall_thickness_cm, number_of_balls):
    total_volume_liters = 0.0
    
    inner_radius_cm = inner_diameter_first_ball_cm / 2
    
    for _ in range(number_of_balls):
        outer_radius_cm = inner_radius_cm + wall_thickness_cm
        
        volume_cm_cubed = (4/3) * math.pi * (outer_radius_cm ** 3)
        
        volume_liters = volume_cm_cubed / 1000.0
        
        total_volume_liters += volume_liters
        
        inner_radius_cm = outer_radius_cm
    
    return total_volume_liters

total_volume = calculate_total_volume(inner_diameter_first_ball_cm, wall_thickness_cm, number_of_balls)

print(f"Суммарный объем всех шаров составляет {total_volume:.2f} литров.")