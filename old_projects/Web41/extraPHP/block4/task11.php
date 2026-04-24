<?php
$volume1 = (float)readline("Введите объем первого тела: ");
$mass1 = (float)readline("Введите массу первого тела: ");
$volume2 = (float)readline("Введите объем второго тела: ");
$mass2 = (float)readline("Введите массу второго тела: ");
$density1 = $mass1 / $volume1;
$density2 = $mass2 / $volume2;
if ($density1 > $density2) {
    echo "Материал первого тела имеет большую плотность";
} else {
    echo "Материал второго тела имеет большую плотность";
}
?>