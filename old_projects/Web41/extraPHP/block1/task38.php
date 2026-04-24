<?php
$sequence = '';
for ($i = 101; $i <= 150; $i++) {
    $sequence .= $i;
}
function getKthDigit($k) {
    global $sequence;

    if ($k < 1 || $k > 150) {
        return "Значение k должно быть в диапазоне от 1 до 150.";
    }

    $kthDigit = $sequence[$k - 1]; 

    if ($k % 3 === 0) {
        return "k = $k (кратное 3): k-я цифра = $kthDigit";
    } elseif ($k % 3 === 1) { // 1, 4, 7...
        return "k = $k (представляющее 1, 4, 7...): k-я цифра = $kthDigit";
    } elseif ($k % 3 === 2) { // 2, 5, 8...
        return "k = $k (представляющее 2, 5, 8...): k-я цифра = $kthDigit";
    }
}

$k = 7; 
$result = getKthDigit($k);
echo $result . "\n";
?>