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


$result1 = !$A && $B;        
$result2 = $A || !$B;       
$result3 = $A && $B || $C;   

echo "Не A и B: " . ($result1 ? "Истина" : "Ложь") . PHP_EOL;
echo "A или не B: " . ($result2 ? "Истина" : "Ложь") . PHP_EOL;
echo "A и B или C: " . ($result3 ? "Истина" : "Ложь") . PHP_EOL;
?>
</body>
</html>