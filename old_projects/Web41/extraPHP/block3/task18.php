<?php

$values = [false, true];

echo "X\tY\t! (X and !Y)\tA = ! (X and !Y) or X\t!X\tY and !X\tB = (Y and !X) or !Y\t!Y\t!Y and !X\tC = (!Y and !X) or Y\n";

foreach ($values as $X) {
    foreach ($values as $Y) {
        $not_Y = !$Y;
        $not_X = !$X;

        $x_and_not_y = $X && $not_Y;
        $not_x_and_not_y = !$x_and_not_y;

        $expr_a = $not_x_and_not_y || $X;

        $y_and_not_x = $Y && $not_X;
        $expr_b = $y_and_not_x || !$Y;

        $not_y_and_not_x = $not_Y && $not_X;
        $expr_c = $not_y_and_not_x || $Y;

        echo ($X ? 'true' : 'false') . "\t" .
             ($Y ? 'true' : 'false') . "\t" .
             ($not_x_and_not_y ? 'true' : 'false') . "\t\t" .
             ($expr_a ? 'true' : 'false') . "\t\t\t" .
             ($not_X ? 'true' : 'false') . "\t" .
             ($y_and_not_x ? 'true' : 'false') . "\t" .
             ($expr_b ? 'true' : 'false') . "\t\t" .
             ($not_Y ? 'true' : 'false') . "\t" .
             ($not_y_and_not_x ? 'true' : 'false') . "\t" .
             ($expr_c ? 'true' : 'false') . "\n";
    }
}
?>
