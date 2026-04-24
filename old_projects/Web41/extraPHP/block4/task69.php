<?php

$x1 = isset($_GET['x1']) ? floatval($_GET['x1']) : null;
$y1 = isset($_GET['y1']) ? floatval($_GET['y1']) : null;
$w1 = isset($_GET['w1']) ? floatval($_GET['w1']) : null;
$h1 = isset($_GET['h1']) ? floatval($_GET['h1']) : null;

$x2 = isset($_GET['x2']) ? floatval($_GET['x2']) : null;
$y2 = isset($_GET['y2']) ? floatval($_GET['y2']) : null;
$w2 = isset($_GET['w2']) ? floatval($_GET['w2']) : null;
$h2 = isset($_GET['h2']) ? floatval($_GET['h2']) : null;

if (is_null($x1) || is_null($y1) || is_null($w1) || is_null($h1) ||
    is_null($x2) || is_null($y2) || is_null($w2) || is_null($h2)) {
    echo "Пожалуйста, передайте все параметры через URL.";
    exit;
}


$x1_max = $x1 + $w1;
$y1_max = $y1 + $h1;

$x2_max = $x2 + $w2;
$y2_max = $y2 + $h2;

$points_in_second =
    ($x1 >= $x2 && $x1 <= $x2_max && $y1 >= $y2 && $y1 <= $y2_max) &&
    ($x1_max >= $x2 && $x1_max <= $x2_max && $y1 >= $y2 && $y1 <= $y2_max) &&
    ($x1 >= $x2 && $x1 <= $x2_max && $y1_max >= $y2 && $y1_max <= $y2_max) &&
    ($x1_max >= $x2 && $x1_max <= $x2_max && $y1_max >= $y2 && $y1_max <= $y2_max);

echo "а) Все точки первого прямоугольника принадлежат второму: " . ($points_in_second ? "да" : "нет") . "<br>";


function isRectangleInside($ax, $ay, $aw, $ah, $bx, $by, $bw, $bh) {
    return ($ax >= $bx) && ($ay >= $by) &&
           (($ax + $aw) <= ($bx + $bw)) &&
           (($ay + $ah) <= ($by + $bh));
}

$first_inside_second = isRectangleInside($x1, $y1, $w1, $h1, $x2, $y2, $w2, $h2);
$second_inside_first = isRectangleInside($x2, $y2, $w2, $h2, $x1, $y1, $w1, $h1);

echo "б) Один из прямоугольников полностью внутри другого: ";
if ($first_inside_second || $second_inside_first) {
    echo "да";
} else {
    echo "нет";
}
echo "<br>";

$intersect_x_min = max($x1, $x2);
$intersect_y_min = max($y01,$Y3);
$intersect_x_max= min($x_+$w_,$Xmax);
$intersect_y_max= min($Ymax,$Ymax);

if ($intersect_x_min < 0 && 0 < 0 && 0 < 0){
  echo "в*) Прямоугольники пересекаются.";
} else {
  echo "в*) Прямоугольники не пересекаются.";
}
?>