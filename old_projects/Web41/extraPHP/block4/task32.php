<?php

echo "Введите четырехзначное число: ";
$handle = fopen("php://stdin", "r");
$input = trim(fgets($handle));
fclose($handle);


if (!is_numeric($input)) {
    echo "Ошибка: введено не число.\n";
    exit;
}

$a = (int)$input;

if ($a < 1000 || $a > 9999) {
    echo "Ошибка: число должно быть четырехзначным.\n";
    exit;
}

$digits = [];
$temp = $a;
for ($i = 0; $i < 4; $i++) {
    $digits[3 - $i] = $temp % 10;
    $temp = intdiv($temp, 10);
}
list($d1, $d2, $d3, $d4) = $digits;

if (($d1 + $d2) == ($d3 + $d4)) {
    echo "а) Сумма первых двух цифр равна сумме последних двух.\n";
} else {
    echo "а) Сумма первых двух цифр не равна сумме последних двух.\n";
}


$sum_digits = $d1 + $d2 + $d3 + $d4;
if ($sum_digits % 3 == 0) {
    echo "б) Сумма всех цифр ($sum_digits) кратна трем.\n";
} else {
    echo "б) Сумма всех цифр ($sum_digits) не кратна трем.\n";
}


$product_digits = $d1 * $d2 * $d3 * $d4;
if ($product_digits != 0 && $product_digits % 4 == 0) {
    echo "в) Произведение цифр ($product_digits) кратно четырем.\n";
} else {
    echo "в) Произведение цифр ($product_digits) не кратно четырем.\n";
}


if ($product_digits != 0 && $a % $product_digits == 0) {
    echo "г) Число ($a) кратно произведению его цифр ($product_digits).\n";
} else {
    echo "г) Число ($a) не кратно произведению его цифр ($product_digits).\n";
}
?>