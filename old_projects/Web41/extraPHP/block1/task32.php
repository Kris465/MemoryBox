<?php
function findOriginalNumber() {
    for ($c = 1; $c <= 9; $c++) {
        $remaining = 654 - 100 * $c;
        
        if ($remaining < 10 || $remaining > 99) {
            continue; 
        }
        $b = (int)($remaining / 10);
        $a = $remaining % 10;

        if ($a >= 0 && $a <= 9 && $b >= 0 && $b <= 9) {
            $x = 100 * $a + 10 * $b + $c; 
            return $x;
        }
    }
    return null; 
}

$originalNumber = findOriginalNumber();

if ($originalNumber !== null) {
    echo "Оригинальное число x: " . $originalNumber . "\n";
} else {
    echo "Оригинальное число x не найдено.\n";
}
?>