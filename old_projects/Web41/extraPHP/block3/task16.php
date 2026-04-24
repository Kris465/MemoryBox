<?php

$values = [false, true];

echo "X\tY\t!X and !Y\tX or (!X and Y)\t(!X and Y) or Y\n";

foreach ($values as $X) {
    foreach ($values as $Y) {
        $not_X = !$X;
        $not_Y = !$Y;

        $expr_a = $not_X && $not_Y;
        $expr_b = $X || ($not_X && $Y);
        $expr_c = ($not_X && $Y) || $Y;

        echo ($X ? 'true' : 'false') . "\t" .
             ($Y ? 'true' : 'false') . "\t" .
             ($expr_a ? 'true' : 'false') . "\t\t" .
             ($expr_b ? 'true' : 'false') . "\t\t" .
             ($expr_c ? 'true' : 'false') . "\n";
    }
}
?>