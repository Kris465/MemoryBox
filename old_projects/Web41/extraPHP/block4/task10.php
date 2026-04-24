<?php
$radius = (float)readline("Введите радиус круга: ");
$side = (float)readline("Введите сторону квадрата: ");
$areaCircle = pi() * $radius * $radius;
$areaSquare = $side * $side;
if ($areaCircle > $areaSquare) {
    echo "Площадь круга больше";
} else {
    echo "Площадь квадрата больше";
}
?>