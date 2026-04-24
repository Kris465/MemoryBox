<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка размещения прямоугольников</title>
</head>
<body>
<h2>Можно ли разместить прямоугольник со сторонами a, b внутри прямоугольника со сторонами c, d</h2>
<form method="post">
a: <input type="number" step="any" name="a" required><br><br>
b: <input type="number" step="any" name="b" required><br><br>
c: <input type="number" step="any" name="c" required><br><br>
d: <input type="number" step="any" name="d" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);
$c = floatval($_POST['c']);
$d = floatval($_POST['d']);

if (($a <= $c && $b <= $d) || ($a <= $d && $b <= $c)) {
    echo "<p>Можно разместить прямоугольник со сторонами a, b внутри другого.</p>";
} else {
    echo "<p>Нельзя разместить прямоугольник со сторонами a, b внутри другого.</p>";
}
}
?>
</body>
</html>