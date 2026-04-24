<?php
function findOriginalNumber($n) {
    for ($x = 100; $x < 1000; $x++) {
        $hundreds = (int)($x / 100); 
        $tens = (int)(($x / 10) % 10); 
        $units = $x % 10; 

        $newNumber = $hundreds * 10 + $units;

        if ($newNumber * 10 + $tens === $n) {
            return $x;
        }
    }

    return null;

}

$n = (int)readline("Введите трехзначное число n (100 ≤ n ≤ 999): ");

if ($n < 100 || $n > 999) {
    echo "Ошибка: число должно быть в диапазоне от 100 до 999.\n";
} else {
    $originalNumber = findOriginalNumber($n);
    
    if ($originalNumber !== null) {
        echo "Оригинальное число x: " . $originalNumber . "\n";
    } else {
        echo "Оригинальное число x не найдено.\n";
    }
}
?>