<?php
$x = floatval(readline("Введите значение x: "));

$sin_x = sin($x);

if ($sin_x > 0) {
    $k = 2;
} elseif ($sin_x < 0) {
    $k = 3;
} else {
    $k = 1;
}

$f_x = $k * $x;

echo "Значение функции f(x): " . $f_x . "\n";
?>