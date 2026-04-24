<?php
for ($x = 100; $x < 1000; $x++) {
    $c = $x % 10;

    $result = $x - $c;

    $quotient = $result / 10;

    $newNumber = ($c * 100) + $quotient; 
    
    // Проверяем условие
    if ($newNumber == 237) {
        echo "Найдено число x: " . $x . "\n";
        break; 
    }
}
?>