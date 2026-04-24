<?php

$X = true;
$Y = true;
$Z = false;


$result_a = (int)(!$X && $Y);      
$result_b = (int)($X || !$Y);      
$result_c = (int)($X || $Y && $Z); 


echo "а) не X и Y: " . $result_a . "\n";
echo "б) X или не Y: " . $result_b . "\n";
echo "в) X или Y и Z: " . $result_c . "\n";
?>