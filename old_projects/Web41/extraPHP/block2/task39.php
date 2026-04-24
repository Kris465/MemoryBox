<?php

function calculateHourAngle($h, $m, $s)
{
    $hourDegrees = $h * 30;
    
    $minuteDegrees = $m * 0.5;
    $secondDegrees = $s / 120;
    
    return ($hourDegrees + $minuteDegrees + $secondDegrees);
}

$h = 10;
$m = 15;
$s = 45;

$angle = calculateHourAngle($h, $m, $s);
echo "Угол между начальной позицией часовой стрелки и указанным временем составляет: " . round($angle, 2) . " градусов.";