<?php
$values = [true, false];

echo "Таблица истинности:\n";
echo "A\tB\tC\tне (A или не B и C)\tA и не (B или не C)\tне (не A или B и C)\n";
echo "--------------------------------------------------------------------------------\n";

foreach ($values as $A) {
    foreach ($values as $B) {
        foreach ($values as $C) {
            $result_a = !($A || (!$B && $C));

            $result_b = $A && !($B || !$C);
            
            $result_c = !(!$A || ($B && $C));
            
            echo $A ? 'true' : 'false';
            echo "\t";
            echo $B ? 'true' : 'false';
            echo "\t";
            echo $C ? 'true' : 'false';
            echo "\t";
            echo $result_a ? '        true        ' : '        false       ';
            echo "\t";
            echo $result_b ? '        true        ' : '        false       ';
            echo "\t";
            echo $result_c ? '        true        ' : '        false       ';
            echo "\n";
        }
    }
}
?>