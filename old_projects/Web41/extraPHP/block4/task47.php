<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка равнобедренного треугольника</title>
</head>
<body>
<h2>Проверка, является ли треугольник со сторонами a, b, c равнобедренным</h2>
<form method="post">
a: <input type="number" step="any" name="a" required><br><br>
b: <input type="number" step="any" name="b" required><br><br>
c: <input type="number" step="any" name="c" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);
$c = floatval($_POST['c']);

if ($a > 0 && $b > 0 && $c > 0 && (($a == $b) || ($a == $c) || ($b == $c))) {
    echo "<p>Треугольник равнобедренный.</p>";
} else {
    echo "<p>Треугольник не является равнобедренным.</p>";
}
}
?>
</body>
</html>