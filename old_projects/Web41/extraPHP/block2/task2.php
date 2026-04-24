<?php
$X = false; 
$Y = true; 
$Z = false; 

$result1 = $X || $Z; 
$result2 = $X && $Y; 
$result3 = $X && $Z; 

echo "X или Z: " . ($result1 ? "Истина" : "Ложь") . PHP_EOL;
echo "X и Y: " . ($result2 ? "Ложь" : "Истина") . PHP_EOL;
echo "X и Z: " . ($result3 ? "Ложь" : "Ложь") . PHP_EOL;
?>