<?php
echo "Введите время в минутах с начала часа: ";
$handle = fopen("php://stdin", "r");
$t_input = trim(fgets($handle));
fclose($handle);

if (!is_numeric($t_input) || $t_input < 0 || $t_input >= 60) {
    echo "Ошибка: введите число от 0 до 59.999...\n";
    exit;
}

$t = floatval($t_input);


$cycle_duration = 5; 
$green_duration = 3; 

$position_in_cycle = fmod($t, $cycle_duration);

if ($position_in_cycle < $green_duration) {
    echo "В этот момент горит зеленый сигнал.\n";
} else {
    echo "В этот момент горит красный сигнал.\n";
}
?>