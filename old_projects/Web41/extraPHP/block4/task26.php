<?php
$number = 42;

$digit1 = (int)($number / 10);
$digit2 = $number % 10;

$sum_digits = $digit1 + $digit2;

$is_divisible_by_3 = ($sum_digits % 3 === 0);

$a = 5; 

$is_divisible_by_a = ($a != 0) && ($number % $sum_digits === 0);

echo "Число: $number\n";
echo "Сумма цифр: $sum_digits\n";

if ($is_divisible_by_3) {
    echo "Сумма цифр кратна 3.\n";
} else {
    echo "Сумма цифр не кратна 3.\n";
}

if ($is_divisible_by_a) {
    echo "Число кратно сумме цифр и числу a.\n";
} else {
    echo "Число не кратно сумме цифр или числу a.\n";
}
?>