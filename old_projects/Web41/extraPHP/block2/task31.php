<?php
echo "Введите число n (100 ≤ n ≤ 999): ";
$n = intval(trim(fgets(STDIN))); 

if ($n < 100 || $n > 999) {
    echo "Ошибка: число должно быть в диапазоне от 100 до 999.\n";
    exit;
}

$found = false;
for ($x = 100; $x <= 999; $x++) {
    $a = (int)($x / 100);
    $b = (int)(($x % 100) / 10);
    $c = $x % 10; 

    $newNumber = ($a * 10) + $c; 
    $result = ($newNumber * 10) + $b; 

    if ($result == $n) {
        echo "Найдено число x: " . $x . "\n";
        $found = true;
    }
}

if (!$found) {
    echo "Число x не найдено для заданного условия.\n";
}
?>