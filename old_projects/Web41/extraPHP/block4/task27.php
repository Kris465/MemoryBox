<?php

$number = 123; 

if ($number < 100 || $number > 999) {
    echo "Число должно быть трёхзначным.\n";
    exit;
}


$hundreds = (int)($number / 100);
$tens = (int)(($number % 100) / 10);
$units = $number % 10;

if ($hundreds == $units) {
    echo "Число $number является палиндромом.\n";
} else {
    echo "Число $number не является палиндромом.\n";
}
?>