<?php

$A = true;
$B = false;
$C = false;

$result_a = (int)($A || $B); 
$result_b = (int)($A && $B);  
$result_c = (int)($B || $C);
echo "а) А или В: " . $result_a . "\n";
echo "б) А и В: " . $result_b . "\n";
echo "в) В или С: " . $result_c . "\n";
?>