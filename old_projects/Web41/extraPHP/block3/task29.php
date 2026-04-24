<?php

function getNumberInput($prompt) {
    $input = readline($prompt);
    return (float)$input;
}

$X = getNumberInput("Введите число X: ");
$Y = getNumberInput("Введите число Y: ");
$Z = getNumberInput("Введите число Z: ");

$condition_a = ($X % 2 !== 0) && ($Y % 2 !== 0);
$condition_b = ($X < 20) ^ ($Y < 20);
$condition_c = ($X === 0) || ($Y === 0);
$condition_d = ($X < 0) && ($Y < 0) && ($Z < 0);
$condition_e = (($X % 5 === 0 ? 1 : 0) + ($Y % 5 === 0 ? 1 : 0) + ($Z % 5 === 0 ? 1 : 0)) === 1;
$condition_f = ($X > 100) || ($Y > 100) || ($Z > 100);

echo "\nРезультаты:\n";
echo "a) Каждое из чисел X и Y нечетное: " . ($condition_a ? 'true' : 'false') . "\n";
echo "b) Только одно из чисел X и Y меньше 20: " . ($condition_b ? 'true' : 'false') . "\n";
echo "в) Хотя бы одно из чисел X и Y равно нулю: " . ($condition_c ? 'true' : 'false') . "\n";
echo "г) Каждое из чисел X, Y, Z отрицательное: " . ($condition_d ? 'true' : 'false') . "\n";
echo "д) Только одно из чисел X, Y и Z кратно пяти: " . ($condition_e ? 'true' : 'false') . "\n";
echo "е) Хотя бы одно из чисел X, Y, Z больше 100: " . ($condition_f ? 'true' : 'false') . "\n";
?>