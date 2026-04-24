<?php
$n = intval(readline("Введите двузначное число: "));
$digit1 = intval(substr(strval($n), 0, 1));
$digit2 = intval(substr(strval($n), -1));

$square_n = $n * $n;
$sum_cubes_digits = pow($digit1, 3) + pow($digit2, 3);
if ($square_n == 4 * $sum_cubes_digits) {
    echo "да\n";
} else {
    echo "нет\n";
}
?>