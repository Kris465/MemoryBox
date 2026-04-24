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
$not_Z = !$Z;

$expr_a = !($X || $Y) && ($not_X || $not_Z);

$expr_b = !($not_X && $Y) || ($X && $not_Z);

$expr_c = $X || $not_Y && !($X || $not_Z);

echo "\nРезультаты:\n";
echo "a) ¬(X ∨ Y) ∧ (¬X ∨ ¬Z): " . ($expr_a ? 'true' : 'false') . "\n";
echo "b) ¬(¬X ∧ Y) ∨ (X ∧ ¬Z): " . ($expr_b ? 'true' : 'false') . "\n";
echo "c) X ∨ ¬Y ∧ ¬(X ∨ ¬Z): " . ($expr_c ? 'true' : 'false') . "\n";
?>