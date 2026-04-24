<?php

$n = intval(trim(fgets(STDIN)));


$s = str_pad($n, 4, '0', STR_PAD_LEFT);

$digits = str_split($s);

if (count($digits) === count(array_unique($digits))) {
    echo "Все цифры различны\n";
} else {
    echo "Есть повторяющиеся цифры\n";
}
?>