<?php
$n = intval(readline());

if ($n % 2 == 0) {
    echo "Число является четным\n";
} else {
    echo "Число не является четным\n";
}

if (substr(strval($n), -1) == '7') {
    echo "Число оканчивается цифрой 7\n";
} else {
    echo "Число не оканчивается цифрой 7\n";
}
?>