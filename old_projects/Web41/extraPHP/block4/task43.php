<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка делимости</title>
</head>
<body>
<h2>Проверка делимости чисел a и b</h2>
<form method="post">
a: <input type="number" step="any" name="a" required><br><br>
b: <input type="number" step="any" name="b" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);

if ($a != 0 && $b != 0 && (fmod($a, $b) == 0 || fmod($b, $a) == 0)) {
    echo "<p>Да, одно из чисел является делителем другого.</p>";
} else {
    echo "<p>Нет, ни одно из чисел не является делителем другого.</p>";
}
}
?>
</body>
</html>