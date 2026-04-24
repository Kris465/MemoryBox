<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Решение квадратного уравнения</title>
</head>
<body>
<h2>Решение уравнения 2ax² + bx + c = 0</h2>
<form method="post">
a: <input type="number" step="any" name="a" required><br><br>
b: <input type="number" step="any" name="b" required><br><br>
c: <input type="number" step="any" name="c" required><br><br>
<input type="submit" value="Решить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);
$c = floatval($_POST['c']);

if ($a == 0) {
    if ($b == 0) {
        if ($c == 0) {
            echo "<p>Бесконечно много решений (уравнение 0=0).</p>";
        } else {
            echo "<p>Нет решений (уравнение противоречиво).</p>";
        }
    } else {
        $x = -$c / $b;
        echo "<p>Линейное уравнение, решение: x = " . $x . "</p>";
    }
} else {
    $D = $b * $b - 4 * 2 * $a * $c;
    if ($D > 0) {
        $sqrtD = sqrt($D);
        $x1 = (-$b + $sqrtD) / (4 * $a);
        $x2 = (-$b - $sqrtD) / (4 * $a);
        echo "<p>Два различных корня: x₁ = " . $x1 . ", x₂ = " . $x2 . "</p>";
    } elseif ($D == 0) {
        $x = -$b / (4 * $a);
        echo "<p>Один корень (двойной): x = " . $x . "</p>";
    } else {
        echo "<p>Нет действительных решений.</p>";
    }
}
}
?>
</body>
</html>