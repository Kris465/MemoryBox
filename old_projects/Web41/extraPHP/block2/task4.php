<?php

$X = true;   
$Y = true;  
$Z = false;  

$result1 = !$X && $Y;        
$result2 = $X || !$Y;       
$result3 = $X || ($Y && $Z);

echo "Не X и Y: " . ($result1 ? "Истина" : "Ложь");
echo "X или не Y: " . ($result2 ? "Истина" : "Ложь");
echo "X или (Y и Z): " . ($result3 ? "Истина" : "Ложь");
?>