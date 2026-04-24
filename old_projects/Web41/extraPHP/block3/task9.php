<?php

$X = true;
$Y = false;
$Z = false;

$result_a = (int)(!$X || !$Y || !$Z);            
$result_b = (int)((!$X || !$Y) && ($X || $Y));   
$result_v = (int)(($X && $Y) || ($X && $Z) || !$Z); 

echo "а) не X или не Y или не Z: " . $result_a . "\n";
echo "б) (не X или не Y) и (X или Y): " . $result_b . "\n";
echo "в) X и Y или X и Z или не Z: " . $result_v . "\n";
?>