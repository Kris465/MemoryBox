<?php
if (!isset($_GET['number'])) {
    echo "Пожалуйста, передайте число через параметр 'number' в URL.";
    exit;
}
$n = $_GET['number'];
if (strlen($n) != 6 || !ctype_digit($n)) {
    echo "Введите шестизначное число.";
    exit;
}
$first_three = substr($n, 0, 3);
$last_three = substr($n, 3, 3);
$sum_first = array_sum(str_split($first_three));
$sum_last = array_sum(str_split($last_three));
if ($sum_first == $sum_last) {
    echo "Число счастливое";
} else {
    echo "Число не является счастливым";
}
?>