<?php

$a = intval(readline());
$b = intval(readline());
$c = intval(readline());
$d = intval(readline());

$even_count = 0;

if ($a % 2 == 0) {
    $even_count++;
}
if ($b % 2 == 0) {
    $even_count++;
}
if ($c % 2 == 0) {
    $even_count++;
}
if ($d % 2 == 0) {
    $even_count++;
}

echo $even_count;
?>