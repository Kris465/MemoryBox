<?php


$A = true;  
$B = false; 
$C = false; 


$a_result = $A || !($A && $B) || $C;
$b_result = !$A || $A && ($B || $C);
$c_result = ($A || $B && !$C) && $C;


echo "a) Результат: " . var_export($a_result, true) . "\n";
echo "б) Результат: " . var_export($b_result, true) . "\n";
echo "в) Результат: " . var_export($c_result, true) . "\n";

?>