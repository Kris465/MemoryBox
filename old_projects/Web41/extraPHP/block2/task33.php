<?php

$n = 654; 

if ($n < 1 || $n > 999 || $n % 10 == 0) {
    echo "Ошибка: число должно быть в диапазоне от 1 до 999 и последняя цифра не должна быть равна 0.\n";
    exit;
}


$found = false;
for ($x = 100; $x <= 999; $x++) {
    
    $a = (int)($x / 100);
    $b = (int)(($x % 100) / 10); 
    $c = $x % 10; 

     
    $twoDigitNumber = ($a * 10) + $b; 

    
    $swappedNumber = ($b * 10) + $a;

    
    $result = ($c * 100) + $swappedNumber;

    
    if ($result == $n) {
        echo "Найдено число x: " . $x . "\n";
        $found = true;
        break; 
    }
}

if (!$found) {
    echo "Число x не найдено для заданного условия.\n";
}
?>