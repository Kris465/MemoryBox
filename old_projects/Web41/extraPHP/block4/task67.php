<?php
$k = intval(trim(fgets(STDIN)));
if ($k < 1 || $k > 365) {
    echo "Число k должно быть в диапазоне от 1 до 365.";
    exit;
}
$day_of_week = ($k - 1) % 7;
if ($day_of_week == 5 || $day_of_week == 6) {
    echo "Выходной день";
} else {
    echo "Рабочий день";
}
?>