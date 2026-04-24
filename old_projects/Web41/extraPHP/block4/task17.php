<?php
$areaCircle = floatval(readline());
$areaEquilateralTriangle = floatval(readline());

$radius = sqrt($areaCircle / $pi);
$sideTriangle = sqrt((4 * $areaEquilateralTriangle) / sqrt(3));

$circleFitsInTriangle = (2 * $radius) <= $sideTriangle;
$triangleFitsInCircle = ( (sqrt(3)/6) * pow($sideTriangle, 2) ) <= $pi * pow($radius, 2);

echo "а) Круг поместится в треугольник? " . ($circleFitsInTriangle ? "Да" : "Нет") . "\n";
echo "б) Треугольник поместится в круг? " . ($triangleFitsInCircle ? "Да" : "Нет") . "\n";
?>