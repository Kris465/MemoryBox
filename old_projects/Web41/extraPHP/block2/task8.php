<?php
function getDayOfWeek($k, $d) {
    if ($k < 1 || $k > 365) {
        throw new InvalidArgumentException("k должно быть в диапазоне от 1 до 365");
    }
    if ($d < 1 || $d > 7) {
        throw new InvalidArgumentException("d должно быть в диапазоне от 1 до 7 (1-понедельник, ..., 7-воскресенье)");
    }

    $dayOfWeek = ($k + $d - 2) % 7;

    return $dayOfWeek;
}


echo getDayOfWeek(1, 1) . "\n";   
echo getDayOfWeek(7, 1) . "\n";   
echo getDayOfWeek(8, 1) . "\n";   

echo getDayOfWeek(1, 2) . "\n"; 
echo getDayOfWeek(7, 2) . "\n"; 
echo getDayOfWeek(8, 2) . "\n";   

echo getDayOfWeek(1, 7) . "\n";   
echo getDayOfWeek(7, 7) . "\n"; 
echo getDayOfWeek(8, 7) . "\n";   
?>