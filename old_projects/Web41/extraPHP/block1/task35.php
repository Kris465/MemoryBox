<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
function calculateSumDigits($a, $b) {
  
    $firstNumber = 10 * 2 + $a; 
    $secondNumber = 10 * $b + 1; 

    
    $sum = $firstNumber + $secondNumber; 

    $tens = (int)($sum / 10); 
    $units = $sum % 10; 

    return [$tens, $units];
}


$a = 3; 
$b = 5; 

list($tens, $units) = calculateSumDigits($a, $b);

echo "Цифры числа, равного сумме: " . $tens . " и " . $units . "\n";
?>
    
</body>
</html>