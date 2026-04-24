<?php

function getTimeFromAngle($y)
{

    $hours = floor($y / 30); 
    
   
    $remainingDegrees = $y % 30;
    

    $minutes = floor($remainingDegrees / 0.5);
    
    return [$hours, $minutes];
}


$y = 90; 
list($hours, $minutes) = getTimeFromAngle($y);

echo "Прошло " . $hours . " часов и " . $minutes . " минут."; 
?>