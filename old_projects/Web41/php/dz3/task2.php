<?php

function countMirrorNumbers() {
    $count = 0;
    for ($a = 1; $a <= 9; $a++) { 
        for ($b = 0; $b <= 9; $b++) {
            $count++;
        }
    }
    return $count;
}

function countEvenDigits() {
    $evenDigits = [0, 2, 4, 6, 8];
    $count = 0;

    for ($first = 1; $first <= 8; $first += 2) { 
        foreach ($evenDigits as $second) {
            foreach ($evenDigits as $third) {
                foreach ($evenDigits as $fourth) {
                    $count++;
                }
            }
        }
    }
    return $count;
}

function countOddDigits() {
    $oddDigits = [1, 3, 5, 7, 9];
    return pow(count($oddDigits), 4); 
}

function countDecreasingDigits() {
    $count = 0;
    for ($a = 1; $a <= 9; $a++) {
        for ($b = 0; $b <= 9; $b++) {
            for ($c = 0; $c <= 9; $c++) {
                for ($d = 0; $d <= 9; $d++) {
                    if ($a > $b && $b > $c && $c > $d) {
                        $count++;
                    }
                }
            }
        }
    }
    return $count;
}

echo "c) Зеркальные числа: " . countMirrorNumbers() . "\n";
echo "d) Все цифры четные: " . countEvenDigits() . "\n";
echo "e) Все цифры нечетные: " . countOddDigits() . "\n";
echo "f) Цифры в порядке от большего к меньшему: " . countDecreasingDigits() . "\n";
?>