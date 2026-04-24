<?php
$a = isset($_GET['a']) ? floatval($_GET['a']) : null;
$b = isset($_GET['b']) ? floatval($_GET['b']) : null;

if (is_null($a) || is_null($b)) {
    echo "Пожалуйста, передайте два числа через параметры URL: a и b.";
    exit;
}

$max = $a;
if ($b > $max) {
    $max = $b;
}
echo "Наибольшее: " . $max . "<br>";

$min = $a;
if ($b < $min) {
    $min = $b;
}
echo "Наименьшее: " . $min;
?>