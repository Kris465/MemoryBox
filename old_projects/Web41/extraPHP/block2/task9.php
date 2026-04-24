<?php
function getMonthFromNMonths($n) {
    if ($n < 0) {
        return "Введите неотрицательное число";
    }
    $startYear = 1990;
    $startMonth = 1; 

    $totalMonths = $startMonth + $n;

    $year = $startYear + floor(($totalMonths - 1) / 12);
    $month = ($totalMonths - 1) % 12 + 1; 

    return $month; 
}

$n = 3; 
$x = getMonthFromNMonths($n);
echo "При n = $n значение x равно: $x"; 

$n = 12;
$x = getMonthFromNMonths($n);
echo "\nПри n = $n значение x равно: $x"; 

$n = 24; 
$x = getMonthFromNMonths($n);
echo "\nПри n = $n значение x равно: $x"; 
?>