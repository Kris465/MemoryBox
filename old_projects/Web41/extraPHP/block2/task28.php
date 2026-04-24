<?php

$found = false; 
for ($x = 100; $x <= 999; $x++) {

    $a = (int)($x / 100);
    $b = (int)(($x % 100) / 10); 
    $c = $x % 10; 

   
    $newNumber = ($b * 10) + $c; 
    $result = ($b * 100) + $newNumber; 

    
    if ($result == 546) {
        echo "Найдено число x: " . $x . "\n";
        $found = true;
    }
}

if (!$found) {
    echo "Число x не найдено для заданного условия.\n";
}
?>