<?php
$A = true; 
$B = false; 
$C = false; 

$result1 = $A || $B; 
$result2 = $A && $B; 
$result3 = $B || $C; 

echo "A или B: " . ($result1 ? "Истина" : "Ложь") . PHP_EOL;
echo "A и B: " . ($result2 ? "Истина" : "Ложь") . PHP_EOL;
echo "B или C: " . ($result3 ? "Истина" : "Ложь") . PHP_EOL;
?>