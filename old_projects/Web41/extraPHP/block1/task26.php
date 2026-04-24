<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вычисление диаметра окружности</title>
</head>
<body>
    <h1>Вычисление диаметра окружности</h1>

   
    <form method="post">
        <label for="radius">Введите радиус окружности:</label>
        <input type="number" step="0.01" name="radius" id="radius" required>
        <input type="submit" value="Вычислить диаметр">
    </form>

    <?php
   
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
       
        $radius = floatval($_POST['radius']); 

        
        if ($radius >= 0) {
           
            $diameter = 2 * $radius;
            echo "<h2>Диаметр окружности с радиусом $radius равен $diameter.</h2>";
        } else {
            echo "<h2 style='color: red;'>Ошибка: Радиус окружности не может быть отрицательным.</h2>";
        }
    }
    ?>
</body>
</html>