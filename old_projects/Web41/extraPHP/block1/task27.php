<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Расстояние до линии горизонта</title>
</head>
<body>
    <h1>Вычисление расстояния до линии горизонта</h1>

    <form method="post">
        <label for="height">Введите высоту над Землей (в километрах):</label>
        <input type="number" step="0.01" name="height" id="height" required>
        <input type="submit" value="Вычислить расстояние">
    </form>

    <?php

    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        $height = floatval($_POST['height']); 


        $R = 6350;


        if ($height >= 0) {

            $distance = sqrt(2 * $R * $height);
            

            echo "<h2>Расстояние до линии горизонта с высоты {$height} км составляет " . round($distance, 2) . " км.</h2>";
        } else {
            echo "<h2 style='color: red;'>Ошибка: Высота не может быть отрицательной.</h2>";
        }
    }
    ?>
</body>
</html>
