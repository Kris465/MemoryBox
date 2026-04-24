<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка равных чисел</title>
</head>
<body>
<h2>Проверка наличия равных чисел среди a, b, c</h2>
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

if ($a == $b || $a == $c || $b == $c) {
    echo "<p>Есть хотя бы одна пара равных чисел.</p>";
} else {
    echo "<p>Нет ни одной пары равных чисел.</p>";
}
}
?>
</body>
</html>