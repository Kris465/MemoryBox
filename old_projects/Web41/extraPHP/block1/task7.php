<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Три числа</title>
</head>
<body>
    <h1> Введите три числа </h1>
    <form method="post" action="">
        <input type="number"
name="number1" placeholder="Число 1"
required>
        <input type="number"
name="number2" placeholder="Число 2"
required>
        <input type="number"
name="number3" placeholder="Число 3"
required>
        <button
type="submit">Отправить</button>
    </form>\

<?php
        if ($_SERVER["REQUEST_METHOD"] == "POST")  {
                number1 = $_POST['NUMBER1'];
                number2 = $_POST['NUMBER2'];
                number3 = $_POST['NUMBER3'];
                echo
                htmlspecialchars($number1) . " " .
                htmlspecialchars($number2) . " " .
                htmlspecialchars($number3);
        }
?>
    
</body>
</html>