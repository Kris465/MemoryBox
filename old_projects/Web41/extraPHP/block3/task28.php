<?php

function getNumberInput($prompt) {
    $input = readline($prompt);
    return (float)$input;
}

$A = getNumberInput("Введите число A: ");
$B = getNumberInput("Введите число B: ");
$C = getNumberInput("Введите число C: ");

$condition_a = $A > 100 && $B > 100;
$condition_b = ($A % 2 === 0) ^ ($B % 2 === 0);
$condition_c = $A > 0 || $B > 0;
$condition_d = $A % 3 === 0 && $B % 3 === 0 && $C % 3 === 0;
$less_than_50_count = ($A < 50 ? 1 : 0) + ($B < 50 ? 1 : 0) + ($C < 50 ? 1 : 0);
$condition_e = $less_than_50_count === 1;
$condition_f = $A < 0 || $B < 0 || $C < 0;

echo "\nРезультаты:\n";
echo "a) Каждое из чисел A и B больше 100: " . ($condition_a ? 'true' : 'false') . "\n";
echo "b) Только одно из чисел A и B четное: " . ($condition_b ? 'true' : 'false') . "\n";
echo "в) Хотя бы одно из чисел A и B положительно: " . ($condition_c ? 'true' : 'false') . "\n";
echo "г) Каждое из чисел A, B, C кратно трем: " . ($condition_d ? 'true' : 'false') . "\n";
echo "д) Только одно из чисел A, B и C меньше 50: " . ($condition_e ? 'true' : 'false') . "\n";
echo "е) Хотя бы одно из чисел A, B, C отрицательно: " . ($condition_f ? 'true' : 'false') . "\n";
?>