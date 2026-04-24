<?php

$values = [false, true];

echo "X\tY\t! (X or Y)\t!X and Y\tX and !Y\n";

foreach ($values as $X) {
    foreach ($values as $Y) {
        $not_or = !($X || $Y);
        $not_X_and_Y = (!$X) && $Y;
        $X_and_not_Y = $X && (!$Y);

        echo ($X ? 'true' : 'false') . "\t" .
             ($Y ? 'true' : 'false') . "\t" .
             ($not_or ? 'true' : 'false') . "\t\t" .
             ($not_X_and_Y ? 'true' : 'false') . "\t\t" .
             ($X_and_not_Y ? 'true' : 'false') . "\n";
    }
}
?>

