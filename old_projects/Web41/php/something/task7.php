<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма ввода</title>
</head>
<body>





<h2>Проверка кратности</h2>
<form method="post">
    <label for="firstNumber">Первое число:</label>
    <input type="number" id="firstNumber" name="firstNumber" required><br><br>

    <label for="secondNumber">Второе число:</label>
    <input type="number" id="secondNumber" name="secondNumber" required><br><br>

    <input type="submit" value="Проверить кратность">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['firstNumber']) && isset($_POST['secondNumber'])) {
 
    $firstNumber = intval($_POST['firstNumber']);
    $secondNumber = intval($_POST['secondNumber']);


    if ($secondNumber != 0) {
        if ($firstNumber % $secondNumber == 0) {
            echo "<p>Число $firstNumber кратно числу $secondNumber.</p>";
        } else {
            echo "<p>Число $firstNumber не кратно числу $secondNumber.</p>";
        }
    } else {
        echo "<p>Деление на ноль невозможно.</p>";
    }
}
?>

</body>
</html>