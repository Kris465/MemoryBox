<?php
$kph = (float)readline("Введите скорость в км/ч: ");
$mps = (float)readline("Введите скорость в м/с: ");
$mps_in_kph = $mps * 3.6;
if ($kph > $mps_in_kph) {
    echo "Скорость в км/ч больше";
} else {
    echo "Скорость в м/с больше";
}
?>