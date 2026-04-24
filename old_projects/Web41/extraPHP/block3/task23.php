<?php

$values = [false, true];

echo "A\tB\tC\t¬B\t¬A\t¬(A ∨ (¬B ∧ C)) ∨ C\tA = ¬(A ∨ (¬B ∧ C)) ∨ C\t¬(A ∧ ¬B ∨ C) ∧ B\tB = ¬(A ∧ ¬B ∨ C) ∧ B\t¬(¬A ∨ (B ∧ C)) ∨ A\tC = ¬(¬A ∨ (B ∧ C)) ∨ A\n";

foreach ($values as $A) {
    foreach ($values as $B) {
        foreach ($values as $C) {
            $not_B = !$B; 
            $not_A = !$A; 

            $expr_a_part1 = !($A || ($not_B && $C)); 
            $expr_a = $expr_a_part1 || $C; 

            $expr_b_part1 = ($A && $not_B) || $C; 
            $expr_b = !$expr_b_part1 && $B; 

            $expr_c_part1 = $not_A || ($B && $C); 
            $expr_c = !$expr_c_part1 || $A; 

            echo ($A ? 'true' : 'false') . "\t" .
                 ($B ? 'true' : 'false') . "\t" .
                 ($C ? 'true' : 'false') . "\t" .
                 ($not_B ? 'true' : 'false') . "\t" .
                 ($not_A ? 'true' : 'false') . "\t" .
                 ($expr_a ? 'true' : 'false') . "\t\t" .
                 ($expr_b ? 'true' : 'false') . "\t\t" .
                 ($expr_c ? 'true' : 'false') . "\n";
        }
    }
}
?>