<?php

echo "Введите число: ";
$handle = fopen ("php://stdin","r");
$number = trim(fgets($handle));

if (is_numeric($number)) {

    $number = floatval($number);
    

    if ($number > -5 && $number < 3) {
        echo "Число $number принадлежит интервалу (-5, 3).";
    } else {
        echo "Число $number не принадлежит интервалу (-5, 3).";
    }
} else {
    echo "Пожалуйста, введите корректное число.";
}
?>