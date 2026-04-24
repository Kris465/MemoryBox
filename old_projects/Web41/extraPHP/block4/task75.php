<?php
$a = floatval(readline());
$b = floatval(readline());

$absA = ($a >= 0) ? $a : -$a;
$absB = ($b >= 0) ? $b : -$b;

$halfSumAbs = ($absA + $absB) / 2;
echo "Полусумма абсолютных: " . $halfSumAbs . "\n";

$productAbs = $absA * $absB;
$sqrtProduct = sqrt($productAbs);
echo "Квадратный корень из произведения абсолютных: " . $sqrtProduct;
?>