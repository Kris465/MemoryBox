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
    <label for="firstNumber">Первое число:</label>
    <input type="number" id="firstNumber" name="firstNumber" required><br><br>

    <label for="secondNumber">Второе число:</label>
    <input type="number" id="secondNumber" name="secondNumber" required><br><br>

    <input type="submit" value="Показать квадрат большего числа">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['firstNumber']) && isset($_POST['secondNumber'])) {
    $firstNumber = intval($_POST['firstNumber']);
    $secondNumber = intval($_POST['secondNumber']);

    $greaterNumber = max($firstNumber, $secondNumber);

    $square = $greaterNumber * $greaterNumber;

    echo "<p>Квадрат большего числа ($greaterNumber) равен $square.</p>";
}
?>

</body>
</html>