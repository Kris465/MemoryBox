<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Определение единиц и десятков</title>
</head>
<body>
    <h1>Введите натуральное число (n > 9)</h1>
    <form method="post">
        <input type="number" name="number" min="10" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $inputNumber = $_POST['number'];


        if ($inputNumber > 9) {
 
            $units = $inputNumber % 10;

  
            $tens = ($inputNumber / 10) % 10;

            echo "<h2>Результаты:</h2>";
            echo "Количество единиц: " . htmlspecialchars($units) . "<br>";
            echo "Количество десятков: " . htmlspecialchars($tens) . "<br>";
        } else {
            echo "Ошибка: Введите натуральное число больше 9.<br>";
        }
    }
    ?>
</body>
</html>