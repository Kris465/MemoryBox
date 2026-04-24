<?php
function processTwoDigitNumber($number) {
    if ($number < 10 || $number > 99) {
        throw new InvalidArgumentException("Число должно быть двузначным (10-99)");
    }

    $tens = intdiv($number, 10);   
    $units = $number % 10;          
    $sum = $tens + $units;    
    $product = $tens * $units;  

    return [
        'tens' => $tens,
        'units' => $units,
        'sum' => $sum,
        'product' => $product
    ];
}

$number = 45;
$result = processTwoDigitNumber($number);

echo "Число: $number\n";
echo "а) Число десятков: " . $result['tens'] . "\n";
echo "б) Число единиц: " . $result['units'] . "\n";
echo "в) Сумма цифр: " . $result['sum'] . "\n";
echo "г) Произведение цифр: " . $result['product'] . "\n";
?>