<?php
$km = 10; 
$feet = 30; 

$distanceFeetInKm = $feet * 0.305 / 1000;

if ($km < $distanceFeetInKm) {
    echo "Расстояние в километрах меньше";
} else {
    echo "Расстояние в футах меньше";
}
?>