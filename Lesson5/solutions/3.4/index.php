<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Перевод чисел</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Перевод числа</h1>
        <form method="POST" action="">
            <label for="number">Введите число:</label>
            <input type="number" id="number" name="number" required>
            <input type="submit" value="Перевести">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $number = (int)$_POST['number'];
            $binary = decbin($number);
            $hexadecimal = dechex($number);

            echo "<h2>Результаты:</h2>";
            echo "<p>Десятичное: <strong>$number</strong></p>";
            echo "<p>Двоичное: <strong>$binary</strong></p>";
            echo "<p>Шестнадцатеричное: <strong>$hexadecimal</strong></p>";
        }
        ?>
    </div>
</body>
</html>
