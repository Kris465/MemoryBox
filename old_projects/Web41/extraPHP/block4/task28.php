<?php
$number = 385; 

if ($number < 100 || $number > 999) {
    echo "Число должно быть трёхзначным.\n";
    exit;
}

$hundreds = (int)($number / 100);
$tens = (int)(($number % 100) / 10);
$units = $number % 10;

if ($hundreds > $units) {
    echo "Первая цифра ($hundreds) больше последней ($units).\n";
} elseif ($hundreds < $units) {
    echo "Последняя цифра ($units) больше первой ($hundreds).\n";
} else {
    echo "Первая и последняя цифры равны ($hundreds).\n";
}

if ($hundreds > $tens) {
    echo "Первая цифра ($hundreds) больше второй ($tens).\n";
} elseif ($hundreds < $tens) {
    echo "Вторая цифра ($tens) больше первой ($hundreds).\n";
} else {
    echo "Первая и вторая цифры равны ($hundreds).\n";
}

if ($tens > $units) {
    echo "Вторая цифра ($tens) больше последней ($units).\n";
} elseif ($tens < $units) {
    echo "Последняя цифра ($units) больше второй ($tens).\n";
} else {
    echo "Вторая и последняя цифры равны ($tens).\n";
}
?>