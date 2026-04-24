<?php
function calculateTimeFromAngle($y) {
    if ($y < 0 || $y >= 360) {
        return "Неправильный ввод. Угол должен быть в диапазоне от 0 до 360.";
    }

    $hours = floor($y / 30); 

    $remainingAngle = $y - ($hours * 30);

    $minutes = floor($remainingAngle / 0.5); 
    return [
        'hours' => $hours,
        'minutes' => $minutes
    ];
}

$y = 75.5; 
$result = calculateTimeFromAngle($y);
if (is_array($result)) {
    echo "Прошло полных " . $result['hours'] . " часов и " . $result['minutes'] . " минут с начала суток.\n";
} else {
    echo $result . "\n"; 
}
?>