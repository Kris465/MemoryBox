<?php
function calculateSumDigits($a, $b) {
    
    $firstNumber = 300 + 21 * $a; 
    
    
    $secondNumber = 10 * $b + 1; 
    
    
    $sum = $firstNumber + $secondNumber; 
    
    
    $hundreds = (int)($sum / 100); 
    $tens = (int)($sum / 10) % 10; 
    $units = $sum % 10; 
    
    return [$hundreds, $tens, $units]; 
}


$a = 3; 
$b = 5; 

list($hundreds, $tens, $units) = calculateSumDigits($a, $b);

echo "Цифры числа, равного сумме: " . $hundreds . ", " . $tens . ", " . $units . "\n";
?>