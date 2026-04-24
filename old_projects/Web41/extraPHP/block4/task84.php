<?php
$a = (int)readline();
$b = (int)readline();
$c = (int)readline();
$d = (int)readline();

$sum = 0;

if ($a % 3 == 0) {
    $sum += $a;
}
if ($b % 3 == 0) {
    $sum += $b;
}
if ($c % 3 == 0) {
    $sum += $c;
}
if ($d % 3 == 0) {
    $sum += $d;
}

echo $sum;
?>