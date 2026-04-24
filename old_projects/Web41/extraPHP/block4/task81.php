<?php
$a = floatval(readline());
$b = floatval(readline());
$c = floatval(readline());
$d = floatval(readline());

$count_negative = 0;

if ($a < 0) {
    $count_negative++;
}
if ($b < 0) {
    $count_negative++;
}
if ($c < 0) {
    $count_negative++;
}
if ($d < 0) {
    $count_negative++;
}

echo $count_negative;
?>