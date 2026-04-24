<?php

echo "Введите число a: ";
$handle = fopen("php://stdin", "r");
$a_input = trim(fgets($handle));
echo "Введите число b: ";
$b_input = trim(fgets($handle));
fclose($handle);


if (!is_numeric($a_input) || !is_numeric($b_input) || intval($a_input) != $a_input || intval($b_input) != $b_input) {
    echo "Ошибка: введите целые числа.\n";
    exit;
}

$a = (int)$a_input;
$b = (int)$b_input;

 
if ($a == 0 || $b == 0) {
    echo "Делитель не может быть нулем.\n";
    exit;
}


if ($b % $a == 0) {
    echo "Ответ 1: Число a ($a) является делителем числа b ($b).\n";
} else {
    echo "Ответ 1: Число a ($a) не является делителем числа b ($b).\n";
}


if ($a % $b == 0) {
    echo "Ответ 2: Число b ($b) является делителем числа a ($a).\n";
} else {
    echo "Ответ 2: Число b ($b) не является делителем числа a ($a).\n";
}
?>
