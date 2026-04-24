<?php
function sumDigits($a, $b) {

    $firstNumber = 10 * $a + 2;

    $sum = $firstNumber + $b;

    $tens = (int)($sum / 10);
    $units = $sum % 10; 

    return [$tens, $units];
}

$a = 2;
$b = 3; 

list($tens, $units) = sumDigits($a, $b);

echo "Цифры числа, равного сумме: " . $tens . " и " . $units . "\n";
?>