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


        if ($x == 2 || $x == 4 || $x == 5 || $x == 7) {
            $f = 2;
        } else {
            $f = 4;
        }

        echo "<p>Для x = $x, значение функции f(x) = $f.</p>";
    }
    ?>
</body>
</html>