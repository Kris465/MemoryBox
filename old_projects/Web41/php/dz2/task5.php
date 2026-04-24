<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сумма или деление</title>
</head>
<body>

<h2>Введите два числа</h2>
<form method="post">
    <label for="num1">Первое число:</label>
    <input type="number" id="num1" name="num1" required>
    <br>
    <label for="num2">Второе число:</label>
    <input type="number" id="num2" name="num2" required>
    <br>
    <input type="submit" value="Выполнить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $num1 = intval($_POST['num1']);
    $num2 = intval($_POST['num2']);

    
    if ($num1 % 3 === 0 && $num2 % 3 === 0) {
        
        $sum = $num1 + $num2;
        echo "<p>Сумма двух чисел: $sum</p>";
    } else {
       
        if ($num2 != 0) {
           
            $division = $num1 / $num2;
            echo "<p>Результат деления первого числа на второе: $division</p>";
        } else {
            
            echo "<p>Некорректный ввод: второе число не должно быть равно нулю.</p>";
        }
    }
}
?>

</body>
</html>