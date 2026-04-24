<?php

function getIntegerInput($prompt) {
    $input = readline($prompt);
    return (int)$input;
}

$A = getIntegerInput("Введите целое число A: ");

$condition_a = ($A % 2 === 0) || ($A % 3 === 0);
$condition_b = ($A % 3 !== 0) && ($A % 10 === 0);

echo "\nРезультаты:\n";
echo "a) Целое A кратно двум или трем: " . ($condition_a ? 'true' : 'false') . "\n";
echo "б) Целое A не кратно трем и оканчивается нулем: " . ($condition_b ? 'true' : 'false') . "\n";
?>