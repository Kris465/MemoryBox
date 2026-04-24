<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка прохождения головы Васи через форточку</title>
</head>
<body>
<h2>Можно ли Васе высунуть голову в форточку с зазором 1 см с каждой стороны</h2>
<form method="post">
a (размер форточки по одной стороне): <input type="number" step="any" name="a" required><br><br>
b (размер форточки по другой стороне): <input type="number" step="any" name="b" required><br><br>
d (диаметр головы Васи): <input type="number" step="any" name="d" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);
$d = floatval($_POST['d']);

$minA = $a - 2; 
$minB = $b - 2;

if ($d <= $minA && $d <= $minB) {
    echo "<p>Вася сможет высунуть голову через форточку.</p>";
} else {
    echo "<p>Вася не сможет высунуть голову через форточку.</p>";
}
}
?>
</body>
</html>