<?php

$X = false;
$Y = true;
$Z = false;


$result_a = (int)($X || $Z);  
$result_b = (int)($X && $Y);  
$result_c = (int)($X && $Z);  


echo "а) X или Z: " . $result_a . "\n";
echo "б) X и Y: " . $result_b . "\n";
echo "в) X и Z: " . $result_c . "\n";
?>