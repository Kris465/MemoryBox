<?php
$sequence = '';
for ($i = 10; $i < 100; $i++) {
    $sequence .= $i;
}

function analyzeNumber($k) {
    global $sequence;

    $pairIndex = (intval($k / 2)) + 1;
    $pairStartIndex = ($pairIndex - 1) * 2;

    $twoDigitNumber = substr($sequence, $pairStartIndex, 2);

    $kthDigit = $sequence[$k - 1]; 

    return [
        'pair_index' => $pairIndex,
        'two_digit_number' => $twoDigitNumber,
        'kth_digit' => $kthDigit,
    ];
}

$k = 21; 
if ($k < 1 || $k > 180) {
    die("Значение k должно быть в диапазоне от 1 до 180.");
}

$result = analyzeNumber($k);

echo "Номер пары цифр: " . $result['pair_index'] . "\n";
echo "Двузначное число: " . $result['two_digit_number'] . "\n";
echo "k-я цифра: " . $result['kth_digit'] . "\n";
?>