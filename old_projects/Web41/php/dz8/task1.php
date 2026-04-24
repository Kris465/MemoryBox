<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Калькулятор</title>
</head>
<body>

<h1>Простой калькулятор</h1>
<form method="post">
    <label for="num1">Первое число:</label>
    <input type="number" name="num1" required><br><br>
    
    <label for="num2">Второе число:</label>
    <input type="number" name="num2" required><br><br>
    
    <label for="operation">Операция:</label>
    <select name="operation" required>
        <option value="+">Сложение</option>
        <option value="-">Вычитание</option>
        <option value="*">Умножение</option>
        <option value="/">Деление</option>
    </select><br><br>
    
    <input type="submit" value="Вычислить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $operation = $_POST['operation'];

    function calculate($num1, $num2, $operation) {
        switch ($operation) {
            case '+':
                return $num1 + $num2;
            case '-':
                return $num1 - $num2;
            case '*':
                return $num1 * $num2;
            case '/':
                if ($num2 == 0) {
                    return "Ошибка: Деление на ноль невозможно.";
                }
                return $num1 / $num2;
            default:
                return "Ошибка: Некорректное действие.";
        }
    }

    
    $result = calculate($num1, $num2, $operation);

    $displayNum2 = $num2 < 0 ? abs($num2) : $num2;

    
    echo "<h2>Результат:</h2>";
    echo "$num1 $operation $displayNum2 = $result<br>";
}
?>

</body>
</html>