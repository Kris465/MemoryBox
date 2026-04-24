<?php

$A = false;
$B = false;
$C = true;

$result_a = (int)(!$A || !$B || !$C);            
$result_b = (int)((!$A || !$B) && ($A || $B));   
$result_v = (int)(($A && $B) || ($A && $C) || !$C); 

echo "а) (не A или не B) или не C: " . $result_a . "\n";
echo "б) (не A или не B) и (A или B): " . $result_b . "\n";
echo "в) A и B или A и C или не C: " . $result_v . "\n";
?>