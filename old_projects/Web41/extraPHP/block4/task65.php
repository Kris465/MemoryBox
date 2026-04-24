<?php
if (!isset($_GET['year'])) {
    echo "Пожалуйста, передайте год через параметр 'year' в URL.";
    exit;
}
$year = intval($_GET['year']);
if ($year % 400 == 0 || ($year % 4 == 0 && $year % 100 != 0)) {
    echo "Високосный год";
} else {
    echo "Не високосный год";
}
?>