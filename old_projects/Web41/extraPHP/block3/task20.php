<?php

$values = [true, false];

echo "Таблица истинности:\n";
echo "X\tY\tне (не X или Y) или не X\tне (не X и не Y) и X\tне (X или не Y) или не Y\n";
echo "----------------------------------------------------------------------------------------\n";

foreach ($values as $X) {
    foreach ($values as $Y) {
        $result_a = !(!$X || $Y) || !$X;
        
        $result_b = !(!$X && !$Y) && $X;
        
        $result_c = !($X || !$Y) || !$Y;
        
        echo $X ? 'true' : 'false';
        echo "\t";
        echo $Y ? 'true' : 'false';
        echo "\t";
        echo $result_a ? '            true            ' : '            false           ';
        echo "\t";
        echo $result_b ? '            true            ' : '            false           ';
        echo "\t";
        echo $result_c ? '            true            ' : '            false           ';
        echo "\n";
    }
}
?>