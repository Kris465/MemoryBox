<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Калькулятор</title>
</head>
<body>
    <h1>Калькулятор</h1>
    <form method="post" action="">
        <label for="num1">Первое число:</label>
        <input type="text" id="num1" name="num1" required>
        <br><br>

        <label for="num2">Второе число:</label>
        <input type="text" id="num2" name="num2" required>
        <br><br>

        <label for="operation">Действие (+, -, *, /):</label>
        <input type="text" id="operation" name="operation" required>
        <br><br>

        <input type="submit" value="Вычислить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];
        $operation = $_POST['operation'];

        function calculate($num1, $num2, $operation) {
            if (!is_numeric($num1) || !is_numeric($num2)) {
                return "Ошибка: оба аргумента должны быть числами.";
            }

            switch ($operation) {
                case '+':
                    return $num1 + $num2;
                case '-':
                    return $num1 - $num2;
                case '*':
                    return $num1 * $num2;
                case '/':
                    if ($num2 == 0) {
                        return "Ошибка: деление на ноль невозможно.";
                    }
                    return $num1 / $num2;
                default:
                    return "Ошибка: некорректное действие. Допустимые действия: +, -, *, /.";
            }
        }

        $result = calculate($num1, $num2, $operation);
        echo "<h2>Результат: $result</h2>";
    }
    ?>
</body>
</html>