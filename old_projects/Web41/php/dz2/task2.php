<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Квадрат большего числа</title>
</head>
<body>

<h2>Введите два числа</h2>
<form method="post">
    <label for="number1">Первое число:</label>
    <input type="number" id="number1" name="number1" required><br><br>

    <label for="number2">Второе число:</label>
    <input type="number" id="number2" name="number2" required><br><br>

    <input type="submit" value="Вычислить квадрат">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['number1']) && isset($_POST['number2'])) {
    $number1 = floatval($_POST['number1']);
    $number2 = floatval($_POST['number2']);

    $maxNumber = max($number1, $number2);

    $square = $maxNumber * $maxNumber;

    echo "<p>Квадрат большего числа ($maxNumber) равен $square.</p>";
}
?>

</body>
</html>