<?php

$a = floatval(readline());
$b = floatval(readline());
$c = floatval(readline());
$d = floatval(readline());

$sum = 0;

if ($a > 5) {
    $sum += $a;
}
if ($b > 5) {
    $sum += $b;
}
if ($c > 5) {
    $sum += $c;
}
if ($d > 5) {
    $sum += $d;
}


echo $sum;
?>