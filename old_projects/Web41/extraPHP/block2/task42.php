<?php

function timeToNextEvent($h, $m, $eventType) {
    if ($eventType == 'coincide') {

        for ($t = 0; $t <= 720; $t++) { 
            $mt = $m + $t;
            $ht = $h + floor($mt / 60);
            $mt %= 60;
            if ($mt == $ht % 12) {
                return $t;
            }
        }
    } elseif ($eventType == 'perpendicular') {

        for ($t = 0; $t <= 720; $t++) {
            $mt = $m + $t;
            $ht = $h + floor($mt / 60);
            $mt %= 60;
            $diff = abs(($mt * 6) - ($ht % 12 * 0.5));
            if (($diff % 180) == 90 || ($diff % 180) == 270) {
                return $t;
            }
        }
    }
    return null;
}


$h = 9;
$m = 35;

echo "Наименьшее время до совпадения стрелок: ";
echo timeToNextEvent($h, $m, 'coincide');
echo "\n";

echo "Наименьшее время до перпендикулярности стрелок: ";
echo timeToNextEvent($h, $m, 'perpendicular');
echo "\n";
?>