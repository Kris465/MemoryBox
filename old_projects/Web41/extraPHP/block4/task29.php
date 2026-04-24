<?php
echo "Введите трехзначное число: ";
$handle = fopen("php://stdin", "r");
$input = trim(fgets($handle));
fclose($handle);

if (!is_numeric($input)) {
    echo "Ошибка: введено не число.\n";
    exit;
}

$number = (int)$input;

if ($number < 100 || $number > 999) {
    echo "Ошибка: число должно быть трехзначным.\n";
    exit;
}

$hundreds = (int)($number / 100);
$tens = (int)(($number % 100) / 10);
$units = $number % 10;

$sum_cubes = pow($hundreds, 3) + pow($tens, 3) + pow($units, 3);

$square = $number * $number;

if ($square == $sum_cubes) {
    echo "Квадрат числа $number равен сумме кубов его цифр.\n";
} else {
    echo "Квадрат числа $number не равен сумме кубов его цифр.\n";
}
?>