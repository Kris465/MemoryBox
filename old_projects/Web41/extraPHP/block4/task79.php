<?php
$a = floatval(readline());
$b = floatval(readline());
$c = floatval(readline());

if ($a >= 0) {
    $a = $a * $a;
}
if ($b >= 0) {
    $b = $b * $b;
}
if ($c >= 0) {
    $c = $c * $c;
}

echo "$a\n$b\n$c";
?>