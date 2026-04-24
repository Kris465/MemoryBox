<?php

function timeToNextPositions($h, $m) {

    if ($h < 1 || $h > 12 || $m < 0 || $m > 59) {
        return "Некорректное время!";
    }


    if ($h == 12) {
        $h = 0;
    }

    $minToNextCoincidence = null;
    $minToNextPerpendicular = null;

    for ($i = 0; $i < 720; $i++) { 
        $newM = ($m + $i) % 60;
        $newH = ($h + intval(($m + $i) / 60)) % 12;


        $angleHour = (30 * $newH) + (0.5 * $newM);
        $angleMinute = (6 * $newM);


        if ($angleHour == $angleMinute) {
            $minToNextCoincidence = $i;
            break;
        }


        if (abs($angleHour - $angleMinute) == 90 || abs($angleHour - $angleMinute) == 270) {
            $minToNextPerpendicular = $i;
            if ($minToNextCoincidence === null) {
                $minToNextCoincidence = $i; 
            }
            break;
        }
    }

    return [
        'minutes_to_coincidence' => $minToNextCoincidence,
        'minutes_to_perpendicular' => $minToNextPerpendicular
    ];
}


$h = 3; 
$m = 15; 
$result = timeToNextPositions($h, $m);

if (is_array($result)) {
    echo "До совпадения стрелок: " . $result['minutes_to_coincidence'] . " минут\n";
    echo "До перпендикулярного расположения стрелок: " . $result['minutes_to_perpendicular'] . " минут\n";
} else {
    echo $result;
}

?>