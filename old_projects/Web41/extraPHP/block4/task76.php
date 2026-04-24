<?php
$a = floatval(readline());
$b = floatval(readline());

$absA = ($a >= 0) ? $a : -$a;
$absB = ($b >= 0) ? $b : -$b;

if ($absA > $absB) {
    $a /= 2;
}

echo $a;
?>