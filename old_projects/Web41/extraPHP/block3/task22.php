<?php

$values = [false, true];

echo "X\tY\tZ\t¬Y\t¬X\t¬(X ∨ (¬Y ∧ Z))\tA = ¬(X ∨ (¬Y ∧ Z))\tY ∨ (X ∧ ¬Y) ∨ Z\tB = Y ∨ (X ∧ ¬Y) ∨ Z\t¬((¬X ∧ Y) ∨ Z)\tC = ¬((¬X ∧ Y) ∨ Z)\n";

foreach ($values as $X) {
    foreach ($values as $Y) {
        foreach ($values as $Z) {
            $not_Y = !$Y; 
            $not_X = !$X; 

            $expr_a_part1 = !($not_Y && $Z); 
            $expr_a = !($X || $expr_a_part1); 

            $expr_b_part1 = $X && $not_Y; 
            $expr_b = $Y || $expr_b_part1 || $Z; 

            $expr_c_part1 = ($not_X && $Y) || $Z; 
            $expr_c = !$expr_c_part1;

            echo ($X ? 'true' : 'false') . "\t" .
                 ($Y ? 'true' : 'false') . "\t" .
                 ($Z ? 'true' : 'false') . "\t" .
                 ($not_Y ? 'true' : 'false') . "\t" .
                 ($not_X ? 'true' : 'false') . "\t" .
                 ($expr_a ? 'true' : 'false') . "\t\t" .
                 ($expr_b ? 'true' : 'false') . "\t\t" .
                 ($expr_c ? 'true' : 'false') . "\n";
        }
    }
}
?>