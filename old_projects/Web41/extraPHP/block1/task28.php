<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Объем и площадь боковой поверхности куба</title>
</head>
<body>
    <h1>Вычисление объема и площади боковой поверхности куба</h1>
    
   
    <form method="post">
        <label for="edge">Введите длину ребра куба (в см):</label>
        <input type="number" step="0.01" name="edge" id="edge" required>
        <input type="submit" value="Вычислить">
    </form>
    
    <?php
    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        $edge = floatval($_POST['edge']); 

       
        if ($edge > 0) {
            
            $volume = pow($edge, 3);
            $lateral_surface_area = 4 * pow($edge, 2);

            
            echo "<h2>Результаты:</h2>";
            echo "<p>Объем куба: " . round($volume, 2) . " см³</p>";
            echo "<p>Площадь боковой поверхности куба: " . round($lateral_surface_area, 2) . " см²</p>";
        } else {
            echo "<h2 style='color: red;'>Ошибка: Длина ребра должна быть положительной.</h2>";
        }
    }
    ?>
</body>
</html>