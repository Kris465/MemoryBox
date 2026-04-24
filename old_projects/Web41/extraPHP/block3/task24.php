<?php

function getBooleanInput($prompt) {
    $input = readline($prompt);
    return strtolower($input) === 'true';
}

$X = getBooleanInput("Введите значение X (true/false): ");
$Y = getBooleanInput("Введите значение Y (true/false): ");
$Z = getBooleanInput("Введите значение Z (true/false): ");

$not_X = !$X;
$not_Y = !$Y;

$expr_a_part1 = !($Y || ($not_X && $Z));
$expr_a = $expr_a_part1 || $Z;

$expr_b_part1 = $not_Y || $Z;
$expr_b = $X && !$expr_b_part1 || $Y;

$expr_c_part1 = $X || ($Y && $Z);
$expr_c = !$expr_c_part1 || $not_X;

echo "\nРезультаты:\n";
echo "a) ¬(Y ∨ (¬X ∧ Z)) ∨ Z: " . ($expr_a ? 'true' : 'false') . "\n";
echo "b) X ∧ ¬(¬Y ∨ Z) ∨ Y: " . ($expr_b ? 'true' : 'false') . "\n";
echo "c) ¬(X ∨ (Y ∧ Z)) ∨ ¬X: " . ($expr_c ? 'true' : 'false') . "\n";
?>