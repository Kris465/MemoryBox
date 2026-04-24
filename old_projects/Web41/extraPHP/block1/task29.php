<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Длина окружности и площадь круга</title>
</head>
<body>
    <h1>Вычисление длины окружности и площади круга</h1>
    <form method="post">
        <label for="radius">Введите радиус окружности (в см):</label>
        <input type="number" step="0.01" name="radius" id="radius" required>
        <input type="submit" value="Вычислить">
    </form>
    
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $radius = floatval($_POST['radius']);

        if ($radius > 0) {
            $circumference = 2 * M_PI * $radius;
            $area = M_PI * pow($radius, 2);

            echo "<h2>Результаты:</h2>";
            echo "<p>Длина окружности: " . round($circumference, 2) . " см</p>";
            echo "<p>Площадь круга: " . round($area, 2) . " см²</p>";
        } else {
            echo "<h2 style='color: red;'>Ошибка: Радиус должен быть положительным.</h2>";
        }
    }
    ?>
</body>
</html>