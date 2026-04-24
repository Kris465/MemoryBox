<?php
$m = intval(readline());
$n = intval(readline());

if ($n != 0 && $m % $n == 0) {
    echo $m / $n;
} else {
    echo "$m на $n нацело не делится";
}
?>