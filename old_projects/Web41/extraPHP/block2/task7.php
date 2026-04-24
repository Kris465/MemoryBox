<?php

$A = true;   
$B = false;  
$C = false;  


$result1 = $A || !($A && $B) || $C;           
$result2 = !$A || ($A && ($B || $C));         
$result3 = ($A || ($B && !$C)) && $C;         


echo "A или не (A и B) или C: " . ($result1 ? "Истина" : "Ложь") . PHP_EOL;
echo "не A или A и (B или C): " . ($result2 ? "Истина" : "Ложь") . PHP_EOL;
echo "(A или (B и не C)) и C: " . ($result3 ? "Истина" : "Ложь") . PHP_EOL;
?>