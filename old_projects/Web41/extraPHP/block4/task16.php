<?php
$areaCircle = 78.5;
$areaSquare = 64;  

$radius = sqrt($areaCircle / pi(3,14));

$squareSide = sqrt($areaSquare);
$circleFitsInSquare = (2 * $radius) <= $squareSide;

$diagonalSquare = $squareSide * sqrt(2);
$squareFitsInCircle = $diagonalSquare <= 2 * $radius;

echo "а) Круг поместится в квадрат? " . ($circleFitsInSquare ? "Да" : "Нет") . "\n";
echo "б) Квадрат поместится в круг? " . ($squareFitsInCircle ? "Да" : "Нет") . "\n";
?>