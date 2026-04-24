<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <title>Вычисление функции f(x)</title>
</head>
<body>
    <h2>Вычисление функции f(x)</h2>
    <form method="post">
        Введите число x: <input type="number" name="x" step="any" required>
        <input type="submit" value="Вычислить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $x = floatval($_POST['x']);
        $sin_x = sin($x);

        $epsilon = 1e-9;

        if (abs($sin_x - 0) < $epsilon || abs($sin_x - 0.2) < $epsilon || abs($sin_x - 0.9) < $epsilon) {
            $f = $sin_x;
        } else {
            $f = 1;
        }

        echo "<p>Для x = $x, sin(x) = $sin_x, значение функции f(x) = $f.</p>";
    }
    ?>
</body>
</html>