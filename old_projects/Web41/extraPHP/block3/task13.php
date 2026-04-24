<?php
$values = [true, false];

echo "Таблица истинности:\n";
echo "A\tB\tне (A и B)\tне A или B\tA или не B\n";
echo "-------------------------------------------------\n";

foreach ($values as $A) {
    foreach ($values as $B) {
        $result_a = !($A && $B);
        
        $result_b = !$A || $B;
        
        $result_c = $A || !$B;
        
        echo $A ? 'true' : 'false';
        echo "\t";
        echo $B ? 'true' : 'false';
        echo "\t";
        echo $result_a ? '    true   ' : '   false   ';
        echo "\t";
        echo $result_b ? '    true   ' : '   false   ';
        echo "\t";
        echo $result_c ? '    true   ' : '   false   ';
        echo "\n";
    }
}
?>