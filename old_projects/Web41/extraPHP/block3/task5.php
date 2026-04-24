<?php
$A = true;
$B = false;
$C = false;

$result_a = (int)($A || $B && !$C);      
$result_b = (int)(!$A && !$B);           
$result_v = (int)(!($A && $C) || $B);    
$result_g = (int)($A && !$B || $C);      
$result_d = (int)($A && (!$B || $C));    
$result_e = (int)($A || !($B && $C));    

echo "а) А или В и не С: " . $result_a . "\n";
echo "б) не А и не В: " . $result_b . "\n";
echo "в) не (А и С) или В: " . $result_v . "\n";
echo "г) А и не В или С: " . $result_g . "\n";
echo "д) А и (не В или С): " . $result_d . "\n";
echo "е) А или (не (В и С)): " . $result_e . "\n";
?>