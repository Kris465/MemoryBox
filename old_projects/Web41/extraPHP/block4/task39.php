<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <title>Проверка области I или III</title>
</head>
<body>
    <h2>Проверка попадания точки в области I или III</h2>
    <form method="post">
        Координата X: <input type="number" name="x" step="any" required><br><br>
        Координата Y: <input type="number" name="y" step="any" required><br><br>
        <input type="submit" value="Проверить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $x = $_POST['x'];
        $y = $_POST['y'];

        if ($x > 0 && $y > 0) {
            echo "<p>Точка с координатами ($x; $y) попадает в область I.</p>";
        } elseif ($x < 0 && $y < 0) {
            echo "<p>Точка с координатами ($x; $y) попадает в область III.</p>";
        } else {
            echo "<p>Точка с координатами ($x; $y) не попадает ни в область I, ни в область III.</p>";
        }
    }
    ?>
</body>
</html>