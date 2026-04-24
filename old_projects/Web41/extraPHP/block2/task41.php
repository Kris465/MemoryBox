<?php
function calculateClockHands($y) {
    $pi = pi();
    

    $h = floor(6 * $y / $pi);
    

    $remainingAngle = $y - ($pi / 6) * $h;
    

    $m = floor(30 * $remainingAngle / $pi);
    

    $alpha = ($pi / 30) * $m;
    
    return [
        'hours' => $h,
        'minutes' => $m,
        'minute_angle' => $alpha,
    ];
}

$y = 1.5;
$result = calculateClockHands($y);

echo "Количество полных часов: " . $result['hours'] . "\n";
echo "Количество полных минут: " . $result['minutes'] . "\n";
echo "Угол минутной стрелки (в радианах): " . $result['minute_angle'] . "\n";
?>