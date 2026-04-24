<?php
function calculateHourAngle($h, $m, $s) {
    $hour_angle = ($h % 12) * 30 + ($m * 0.5) + ($s / 120);
    return $hour_angle;
}

$h = 10; 
$m = 30; 
$s = 0;  

if ($h < 0 || $h > 23 || $m < 0 || $m > 59 || $s < 0 || $s > 59) {
    die("Неправильный ввод. Пожалуйста, убедитесь, что значения находятся в заданных диапазонах.");
}

$angle = calculateHourAngle($h, $m, $s);
echo "Угол между началом суток и заданным моментом времени: " . $angle . " градусов\n";
?>