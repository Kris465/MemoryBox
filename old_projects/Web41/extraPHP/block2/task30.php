<?php

$targetNumber = 456;


$found = false; 
for ($x = 100; $x <= 999; $x++) {

    $a = (int)($x / 100); 
    $b = (int)(($x % 100) / 10); 
    $c = $x % 10; 
    $newNumber = ($a * 10) + $c;
    $result = ($newNumber * 10) + $b; 

    if ($result == $targetNumber) {
        echo "Найдено число x: " . $x . "\n";
        $found = true;
    }
}

if (!$found) {
    echo "Число x не найдено для заданного условия.\n";
}
?>