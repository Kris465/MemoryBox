<?php
$a = intval(readline());
$b = intval(readline());

if ($a != 0 && $b % $a == 0) {
    echo "Да, $a является делителем числа $b";
} else {
    echo "Нет, $a не является делителем числа $b";
}
?>