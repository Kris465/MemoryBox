<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
function calculateMinuteAngleAndTime($y) {
    if ($y <= 0 || $y > 2) {
        return "Неправильный ввод. Угол должен быть в диапазоне от 0 до 2.";
    }

  
    $y_degrees = $y * (180 / M_PI);
    
   
    $hours = floor($y_degrees / 30);

   
    $remaining_angle = $y_degrees - ($hours * 30);

   
    $minutes = floor($remaining_angle / 0.5);

   
    $minute_angle = $minutes * 6; 

    return [
        'minute_angle' => $minute_angle,
        'hours' => $hours,
        'minutes' => $minutes
    ];
}


$y = 1.0; 
$result = calculateMinuteAngleAndTime($y);

if (is_array($result)) {
    echo "Угол минутной стрелки: " . $result['minute_angle'] . " градусов\n";
    echo "Прошло полных " . $result['hours'] . " часов и " . $result['minutes'] . " минут.\n";
} else {
    echo $result . "\n"; 
}
?>
</body>
</html>