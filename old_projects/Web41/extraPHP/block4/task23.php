<?php
$n = intval(readline());
$digit1 = intval(substr(strval($n), 0, 1));
$digit2 = intval(substr(strval($n), -1));

if ($digit1 > $digit2) {
    echo "Первая цифра больше второй\n";
} elseif ($digit1 < $digit2) {
    echo "Вторая цифра больше первой\n";
} else {
    echo "Цифры равны\n";
}
?>