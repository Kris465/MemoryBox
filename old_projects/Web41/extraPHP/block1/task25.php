<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Периметр квадрата</title>
</head>
<body>
    <h1>Вычисление периметра квадрата</h1>

    <form method="post">
        <label for="side">Введите длину стороны квадрата:</label>
        <input type="number" step="0.01" name="side" id="side" required>
        <input type="submit" value="Вычислить периметр">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $side = floatval($_POST['side']); 

        if ($side >= 0) {
            $perimeter = 4 * $side;
            echo "<h2>Периметр квадрата с стороной $side равен $perimeter.</h2>";
        } else {
            echo "<h2 style='color: red;'>Ошибка: Сторона квадрата не может быть отрицательной.</h2>";
        }
    }
    ?>
</body>
</html>