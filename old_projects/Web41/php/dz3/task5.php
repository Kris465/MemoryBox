<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Конвертер в римские числа</title>
</head>
<body>

<form method="POST" action="">
    <label for="number">Введите число:</label>
    <input type="number" name="number" id="number" required>
    <input type="submit" value="Преобразовать">
</form>

<?php
function intToRoman($num) {
    $romanNumber = '';
    $romanNumerals = [
        1000 => 'M',
        900 => 'CM',
        500 => 'D',
        400 => 'CD',
        100 => 'C',
        90 => 'XC',
        50 => 'L',
        40 => 'XL',
        10 => 'X',
        9 => 'IX',
        5 => 'V',
        4 => 'IV',
        1 => 'I'
    ];

    foreach ($romanNumerals as $value => $letter) {
        while ($num >= $value) {
            $romanNumber .= $letter;
            $num -= $value;
        }
    }
    return $romanNumber;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = (int)$_POST['number']; 
    if ($number > 0) { 
        $roman = intToRoman($number);
        echo "<p>Римское число: $roman</p>";
    } else {
        echo "<p>Пожалуйста, введите положительное число.</p>";
    }
}
?>

</body>
</html>