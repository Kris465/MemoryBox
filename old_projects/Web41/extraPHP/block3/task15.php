<?php

$values = [false, true];

echo "A\tB\t!A or !B\tA and (A or !B)\t(!A or B) and B\n";

foreach ($values as $A) {
    foreach ($values as $B) {
        $not_A = !$A;
        $not_B = !$B;

        $expr_a = $not_A || $not_B;
        $expr_b = $A && ($A || $not_B);
        $expr_c = ($not_A || $B) && $B;

        echo ($A ? 'true' : 'false') . "\t" .
             ($B ? 'true' : 'false') . "\t" .
             ($expr_a ? 'true' : 'false') . "\t\t" .
             ($expr_b ? 'true' : 'false') . "\t\t\t" .
             ($expr_c ? 'true' : 'false') . "\n";
    }
}
?>