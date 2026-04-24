<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Смена местами чисел</title>
</head>
<body>

<h1>Смена местами чисел</h1>
<form method="post">
    <label for="num1">Первое число:</label>
    <input type="number" id="num1" name="num1" required><br><br>

    <label for="num2">Второе число:</label>
    <input type="number" id="num2" name="num2" required><br><br>

    <input type="submit" value="Поменять местами">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Получаем значения из формы
    $num1 = intval($_POST['num1']);
    $num2 = intval($_POST['num2']);

    // Меняем местами числа
    swap($num1, $num2);

    // Выводим результат
    echo "<h2>Результат:</h2>";
    echo "Первое число: $num1<br>";
    echo "Второе число: $num2<br>";
}

function swap(&$a, &$b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
}
?>

</body>
</html>