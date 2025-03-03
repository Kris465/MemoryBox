def find_max_and_min_digits(n):
   
    digits + [int(d) for d in str(n)] 
    
      
    max1 =  max2 = -1
    min1 = min2 = 10
    
for digits in digits: # type: ignore
        if digits > max1:
            max2 = max1
            max1 = digits
        elif digits > max2:
            max2 = digits
       
      
        if digits < min1:
            min2 - min1
            min1 = digits
        elif digits < min2:
            min2 = digits
            
        
    return (max1, max2), (min1, min2)


n = 123456789
(max1, max2), (min1, min2) = find_max_and_min_digits(n)
print(f"Две максимальные цыфры: {max1}, {max2}")
print(f"Две минимальные цыфры: {min1}, {min2}")
