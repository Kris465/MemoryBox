<?php
$n = intval(readline());
$digit1 = intval(substr(strval($n), 0, 1));
$digit2 = intval(substr(strval($n), -1));
$sum_digits = $digit1 + $digit2;

if ($sum_digits >= 10 && $sum_digits <= 99) {
    echo "Сумма цифр двузначное число\n";
} else {
    echo "Сумма цифр не является двузначным числом\n";
}

if ($n > $sum_digits) {
    echo "Число больше суммы его цифр\n";
} else {
    echo "Число не больше суммы его цифр\n";
}
?>