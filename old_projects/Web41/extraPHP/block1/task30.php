<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вычисление функций</title>
</head>
<body>
    <h1>Вычисление значений функций</h1>
    
    <h2>Функция 1: z = (3^2 + 2.5) * (x + xy) + 1.78</h2>
    <form method="post">
        <label for="x">Введите значение x:</label>
        <input type="number" step="0.01" name="x" id="x" required><br>
        <label for="y">Введите значение y:</label>
        <input type="number" step="0.01" name="y" id="y" required><br>
        <input type="submit" name="calculate1" value="Вычислить z">
    </form>

    <h2>Функция 2: f(a, b) = ((x + 3.56) * a + 3) * (5.8 + 2.5) * (2 + 1)</h2>
    <form method="post">
        <label for="a">Введите значение a:</label>
        <input type="number" step="0.01" name="a" id="a" required><br>
        <label for="b">Введите значение b:</label>
        <input type="number" step="0.01" name="b" id="b" required><br>
        <input type="submit" name="calculate2" value="Вычислить f(a, b)">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST['calculate1'])) {
            $x = floatval($_POST['x']);
            $y = floatval($_POST['y']);
            
            $z = (pow(3, 2) + 2.5) * ($x + $x * $y) + 1.78;
            echo "<h3>Результат функции 1: z = " . round($z, 2) . "</h3>";
        }

        if (isset($_POST['calculate2'])) {
            $a = floatval($_POST['a']);
            $b = floatval($_POST['b']);

            $f = ((floatval($_POST['x']) + 3.56) * $a + 3) * (5.8 + 2.5) * (2 + 1);
            echo "<h3>Результат функции 2: f(a, b) = " . round($f, 2) . "</h3>";
        }
    }
    ?>
</body>
</html>