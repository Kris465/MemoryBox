<?php
$a1 = 2;
$a2 = 1;
$b = 2; 

$sum = ($a1 * 10 + $a2) + $b;

$result_tens = (int)($sum / 10);
$result_units = $sum % 10;

echo "Цифры суммы: десятки - $result_tens, единицы - $result_units";
?>