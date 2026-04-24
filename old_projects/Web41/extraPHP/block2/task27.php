<?php
// Запрашиваем у пользователя ввод числа n
$handle = fopen("php://stdin", "r");
echo "Введите число n (1 ≤ n ≤ 999): ";
$input = fgets($handle);
$n = (int)trim($input);

if ($n < 1 || $n > 999) {
    echo "Ошибка: Введите число в диапазоне от 1 до 999.\n";
    exit;
}

$found = false; 
for ($x = 100; $x <= 999; $x++) {
    $a = (int)($x / 100); 
    $b = (int)(($x / 10) % 10); 
    $c = $x % 10; 

    if ((10 * ($b * 10 + $c)) + $a == $n) {
        echo "Найдено число x: " . $x . "\n";
        $found = true;
    }
}

if (!$found) {
    echo "Число x не найдено для заданного n.\n";
}
?>