<?php
$a = floatval(readline());
$b = floatval(readline());
$c = floatval(readline());
$d = floatval(readline());

$max = $a;
if ($b > $max) {
    $max = $b;
}
if ($c > $max) {
    $max = $c;
}
if ($d > $max) {
    $max = $d;
}
echo "Наибольшее: " . $max . "\n";

$min = $a;
if ($b < $min) {
    $min = $b;
}
if ($c < $min) {
    $min = $c;
}
if ($d < $min) {
    $min = $d;
}
echo "Наименьшее: " . $min . "\n";
?>