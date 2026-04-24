<?php
$x1_left = floatval(readline());
$y1_bottom = floatval(readline());
$width1 = floatval(readline());
$height1 = floatval(readline());

$x2_left = floatval(readline());
$y2_bottom = floatval(readline());
$width2 = floatval(readline());
$height2 = floatval(readline());

$x1_right = $x1_left + $width1;
$y1_top = $y1_bottom + $height1;
$x2_right = $x2_left + $width2;
$y2_top = $y2_bottom + $height2;

$x_min = min($x1_left, $x2_left);
$y_min = min($y1_bottom, $y2_bottom);
$x_max = max($x1_right, $x2_right);
$y_max = max($y1_top, $y2_top);

echo "Левый нижний угол: ($x_min, $y_min)\n";
echo "Правый верхний угол: ($x_max, $y_max)\n";
?>