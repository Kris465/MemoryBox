<?php

function getIntegerInput($prompt) {
    $input = readline($prompt);
    return (int)$input;
}

$N = getIntegerInput("Введите целое число N: ");

$condition_a = ($N % 5 === 0) || ($N % 7 === 0);
$condition_b = ($N % 4 === 0) && ($N % 10 !== 0);

echo "\nРезультаты:\n";
echo "a) Целое N кратно пяти или семи: " . ($condition_a ? 'true' : 'false') . "\n";
echo "б) Целое N кратно четырем и не оканчивается нулем: " . ($condition_b ? 'true' : 'false') . "\n";
?>