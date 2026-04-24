<?php
$a = floatval(readline());
$b = floatval(readline());
$c = floatval(readline());

$max = $a;
if ($b > $max) {
    $max = $b;
}
if ($c > $max) {
    $max = $c;
}
echo "Наибольшее: " . $max . "\n";

$min = $a;
if ($b < $min) {
    $min = $b;
}
if ($c < $min) {
    $min = $c;
}
echo "Наименьшее: " . $min . "\n";
?>