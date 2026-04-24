<?php

$values = [false, true];

echo "A\tB\t¬A\t¬B\t¬(¬A ∧ ¬B)\tA = ¬(¬A ∧ ¬B) ∧ A\t¬(¬A ∨ ¬B)\tB = ¬(¬A ∨ ¬B) ∨ A\t¬(¬A ∨ ¬B)\tC = ¬(¬A ∨ ¬B) ∧ B\n";

foreach ($values as $A) {
    foreach ($values as $B) {
        $not_A = !$A; 
        $not_B = !$B; 

        $expr_a_part1 = !($not_A && $not_B);
        $expr_a = $expr_a_part1 && $A;

        $expr_b_part1 = !($not_A || $not_B); 
        $expr_b = $expr_b_part1 || $A; 

        $expr_c_part1 = !($not_A || $not_B);
        $expr_c = $expr_c_part1 && $B; 

        echo ($A ? 'true' : 'false') . "\t" .
             ($B ? 'true' : 'false') . "\t" .
             ($not_A ? 'true' : 'false') . "\t" .
             ($not_B ? 'true' : 'false') . "\t" .
             ($expr_a_part1 ? 'true' : 'false') . "\t\t" .
             ($expr_a ? 'true' : 'false') . "\t\t" .
             ($expr_b_part1 ? 'true' : 'false') . "\t\t" .
             ($expr_b ? 'true' : 'false') . "\t\t" .
             ($expr_c_part1 ? 'true' : 'false') . "\t\t" .
             ($expr_c ? 'true' : 'false') . "\n";
    }
}
?>