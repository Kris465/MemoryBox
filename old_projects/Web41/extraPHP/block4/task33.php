2<?php

echo "Введите натуральное число: ";
$handle = fopen("php://stdin", "r");
$input = trim(fgets($handle));
fclose($handle);

if (!is_numeric($input) || intval($input) != $input || $input <= 0) {
    echo "Ошибка: введите натуральное число.\n";
    exit;
}

$number = (string)$input;

$last_digit_char = substr($number, -1);
$last_digit = (int)$last_digit_char;

if ($last_digit % 2 == 0) {
    echo "а) Число заканчивается четной цифрой.\n";
} else {
    echo "а) Число не заканчивается четной цифрой.\n";
}

if ($last_digit % 2 != 0) {
    echo "б) Число заканчивается нечетной цифрой.\n";
} else {
    echo "б) Число не заканчивается нечетной цифрой.\n";
}
?>