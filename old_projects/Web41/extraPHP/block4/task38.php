<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <title>Проверка области I</title>
</head>
<body>
    <h2>Проверка попадания точки в область I</h2>
    <form method="post">
        Координата X: <input type="number" name="x" step="any" required><br><br>
        Координата Y: <input type="number" name="y" step="any" required><br><br>
        <input type="submit" value="Проверить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $x = $_POST['x'];
        $y = $_POST['y'];

        if ($x > 0 && $y > 0 && $y < $x) {
            echo "<p>Точка с координатами ($x; $y) попадает в область I.</p>";
        } else {
            echo "<p>Точка с координатами ($x; $y) не попадает в область I.</p>";
        }
    }
    ?>
</body>
</html>