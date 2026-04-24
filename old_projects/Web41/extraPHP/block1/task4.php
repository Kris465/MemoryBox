<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $number = $_POST['number'];


    echo "Вы ввели число: $number - вот какое число Вы ввели";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Ввод числа</title>
</head>
<body>
    <form method="post">
        <label for="number">Введите число:</label>
        <input type="text" id="number" name="number" required>
        <br>
        <input type="submit" value="Отправить">
    </form>
</body>
</html>