<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка неравенств</title>
</head>
<body>
<h2>Проверка неравенств для чисел a, b, c</h2>
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

if ($a < $b && $b < $c) {
echo "<p>а) Выполняется неравенство a < b < c.</p>";
} else {
echo "<p>а) Не выполняется неравенство a < b < c.</p>";
}

if ($b > $a && $a > $c) {
echo "<p>б) Выполняется неравенство b > a > c.</p>";
} else {
echo "<p>б) Не выполняется неравенство b > a > c.</p>";
}
}
?>
</body>
</html>