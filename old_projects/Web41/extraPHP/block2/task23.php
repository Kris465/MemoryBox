<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Определение сотен и тысяч</title>
</head>
<body>
    <h1>Введите натуральное число (n > 999)</h1>
    <form method="post">
        <input type="number" name="number" min="1000" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $inputNumber = $_POST['number'];

        if ($inputNumber > 999) {
            $thousands = floor($inputNumber / 1000) % 10;

            $hundreds = floor($inputNumber / 100) % 10;

            echo "<h2>Результаты:</h2>";
            echo "Количество тысяч: " . htmlspecialchars($thousands) . "<br>";
            echo "Количество сотен: " . htmlspecialchars($hundreds) . "<br>";
        } else {
            echo "Ошибка: Введите натуральное число больше 999.<br>";
        }
    }
    ?>
</body>
</html>