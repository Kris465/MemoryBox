<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $number = $_POST['number'];

    if (ctype_digit($number)) {
        $reversedNumber = strrev($number);
        echo "Число задом наперед: $reversedNumber";
    } else {
        echo "Ошибка: введены нечисловые символы.";
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Переворот числа</title>
</head>
<body>
    <form method="POST" action="">
        <label for="number">Введите число:</label>
        <input type="text" id="number" name="number" required>
        <button type="submit">Отправить</button>
    </form>
</body>
</html>