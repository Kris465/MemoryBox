<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>script</title>
</head>
<body>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number']; 
    $digits = str_split($number); 


    $count = count($digits);
    $sum = 0;
    $maxDigit = 0;
    $minDigit = 9; 


    foreach ($digits as $digit) {
        $digit = (int)$digit; 
        $sum += $digit; 

        if ($digit > $maxDigit) {
            $maxDigit = $digit; 
        }

        if ($digit < $minDigit) {
            $minDigit = $digit; 
        }
    }

    $average = $count > 0 ? $sum / $count : 0;


    echo "<h2>Результаты:</h2>";
    echo "<p>Количество цифр: $count</p>";
    echo "<p>Сумма цифр: $sum</p>";
    echo "<p>Среднее значение: " . round($average, 2) . "</p>";
    echo "<p>Самая большая цифра: $maxDigit</p>";
    echo "<p>Самая маленькая цифра: $minDigit</p>";
} else {

    echo '<form method="post" action="">
            <label for="number">Введите число:</label>
            <input type="text" id="number" name="number" required>
            <input type="submit" value="Обработать">
          </form>';
}
?>
</body>
</html>