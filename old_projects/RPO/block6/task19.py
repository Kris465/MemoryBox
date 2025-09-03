numerator1 = 1
numerator2 = 2
denominator1 = 1
denominator2 = 1

fractions = [(numerator1, denominator1), (numerator2, denominator2)]

current_fraction = (numerator1, denominator2)

found = False

while not found:
    next_numerator = fractions[-1][0] + fractions[-2][0]
    next_denominator = fractions[-1][1] + fractions[-2][1]
    
    fractions.append((next_numerator, next_denominator))
    
    previous_fraction = current_fraction
    current_fraction = (next_numerator, next_denominator)
    
    difference = abs(current_fraction[0] / current_fraction[1] - previous_fraction[0] / previous_fraction[1])
    
    if difference <= 0.001:
        found = True
        
print(f'{current_fraction[0]} / {current_fraction[1]}')