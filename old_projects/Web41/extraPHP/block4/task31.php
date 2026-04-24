<?php
echo "Введите трехзначное число: ";
$handle = fopen("php://stdin", "r");
$input = trim(fgets($handle));
fclose($handle);

if (!is_numeric($input)) {
    echo "Ошибка: введено не число.\n";
    exit;
}

$a = (int)$input;

if ($a < 100 || $a > 999) {
    echo "Ошибка: число должно быть трехзначным.\n";
    exit;
}

$hundreds = (int)($a / 100);
$tens = (int)(($a % 100) / 10);
$units = $a % 10;

if ($hundreds == $tens && $tens == $units) {
    echo "а) Все цифры числа одинаковые.\n";
} else {
    echo "а) Не все цифры числа одинаковые.\n";
}

if ($hundreds == $tens || $tens == $units || $hundreds == $units) {
    echo "б) Среди цифр есть одинаковые.\n";
} else {
    echo "б) Все цифры различны.\n";
}
?>