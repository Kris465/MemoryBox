<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
function swapDigits($number) {

    if ($number < 10 || $number > 99) {
        return "Введите двузначное число.";
    }

  
    $numberStr = (string)$number;

    
    $swappedNumber = $numberStr[1] . $numberStr[0];

    
    return (int)$swappedNumber;
}


$inputNumber = 34; 
$result = swapDigits($inputNumber);
echo "Перестановка цифр числа $inputNumber: $result";
?>
</body>
</html>