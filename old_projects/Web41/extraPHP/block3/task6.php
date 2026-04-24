<?php
$X = false;
$Y = false;
$Z = true;

$result_a = (int)($X || $Y && !$Z);       
$result_b = (int)(!$X && !$Y);           
$result_v = (int)(!($X && $Z) || $Y);    
$result_g = (int)($X && !$Y || $Z);  
$result_d = (int)($X && (!$Y || $Z));      
$result_e = (int)($X || !($Y || $Z));     

echo "а) X или Y и не Z: " . $result_a . "\n";
echo "б) не X и не Y: " . $result_b . "\n";
echo "в) не (X и Z) или Y: " . $result_v . "\n";
echo "г) X и не Y или Z: " . $result_g . "\n";
echo "д) X и (не Y или Z): " . $result_d . "\n";
echo "е) X или (не (Y или Z)): " . $result_e . "\n";
?>