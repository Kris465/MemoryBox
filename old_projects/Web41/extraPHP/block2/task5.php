<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

$A = true;   
$B = false;  
$C = false; 


$result1 = $A || ($B && !$C);         
$result2 = $A && !$B || $C;           
$result3 = !$A && !$B;                
$result4 = !($A && $C) || $B;         
$result5 = $A && (!$B || $C);         
$result6 = $A || !($B && $C);         


echo "A или (B и не C): " . ($result1 ? "Истина" : "Ложь") . PHP_EOL;
echo "A и не B или C: " . ($result2 ? "Истина" : "Ложь") . PHP_EOL;
echo "не A и не B: " . ($result3 ? "Истина" : "Ложь") . PHP_EOL;
echo "не (A и C) или B: " . ($result4 ? "Истина" : "Ложь") . PHP_EOL;
echo "A и (не B или C): " . ($result5 ? "Истина" : "Ложь") . PHP_EOL;
echo "A или (не (B и C)): " . ($result6 ? "Истина" : "Ложь") . PHP_EOL;
?> 
</body>
</html>