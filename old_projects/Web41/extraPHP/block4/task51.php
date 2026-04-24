<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка размещения открытки в конверте</title>
</head>
<body>
<h2>Можно ли разместить открытку внутри конверта с зазором 1 мм с каждой стороны</h2>
<form method="post">
a (размер конверта по одной стороне): <input type="number" step="any" name="a" required><br><br>
b (размер конверта по другой стороне): <input type="number" step="any" name="b" required><br><br>
c (размер открытки): <input type="number" step="any" name="c" required><br><br>
d (размер открытки): <input type="number" step="any" name="d" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);
$c = floatval($_POST['c']);
$d = floatval($_POST['d']);

$minA = $a - 2; 
$minB = $b - 2;

if (($c <= $minA && $d <= $minB) || ($d <= $minA && $c <= $minB)) {
    echo "<p>Открытка поместится в конверт с учетом зазора.</p>";
} else {
    echo "<p>Открытка не поместится в конверт с учетом зазора.</p>";
}
}
?>
</body>
</html>