<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Рисуем фигуры</title>
    <style>
        .circle {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: inline-block;
            margin: 5px;
        }
        .triangle {
            width: 0;
            height: 0;
            border-left: 25px solid transparent;
            border-right: 25px solid transparent;
            border-bottom: 50px solid;
            display: inline-block;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>Введите цвет и фигуру</h1>
    <form method="POST" action="">
        <label for="color">Цвет:</label>
        <input type="text" id="color" name="color" required><br><br>

        <label for="shape">Фигура:</label>
        <select id="shape" name="shape" required>
            <option value="круг">Круг</option>
            <option value="треугольник">Треугольник</option>
        </select><br><br>

        <label for="quantity">Количество:</label>
        <input type="number" id="quantity" name="quantity" min="1" required><br><br>

        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $color = htmlspecialchars($_POST['color']);
        $shape = htmlspecialchars($_POST['shape']);
        $quantity = (int)$_POST['quantity'];

        echo "<h2>Вы ввели:</h2>";
        echo "<p>Цвет: <strong>$color</strong></p>";
        echo "<p>Фигура: <strong>$shape</strong></p>";
        echo "<p>Количество: <strong>$quantity</strong></p>";

        echo "<h2>Рисуем фигуры:</h2>";
        for ($i = 0; $i < $quantity; $i++) {
            if ($shape == "круг") {
                echo "<div class='circle' style='background-color: $color;'></div>";
            } elseif ($shape == "треугольник") {
                echo "<div class='triangle' style='border-bottom-color: $color;'></div>";
            }
        }

        echo "<br><a href='index.php'>Назад</a>";
    }
    ?>
</body>
</html>
