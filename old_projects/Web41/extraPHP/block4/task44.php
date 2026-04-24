<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка остатка при делении</title>
</head>
<body>
<h2>Проверка остатка при делении</h2>
<form method="post">
a: <input type="number" name="a" min="0" required><br><br>
b: <input type="number" name="b" min="1" required><br><br>
c: <input type="number" name="c" required><br><br>
d: <input type="number" name="d" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = intval($_POST['a']);
$b = intval($_POST['b']);
$c = intval($_POST['c']);
$d = intval($_POST['d']);

$remainder = $a % $b;

if ($remainder == $c || $remainder == $d) {
    echo "<p>Верно, при делении остаток равен одному из заданных чисел.</p>";
} else {
    echo "<p>Неверно, при делении остаток не равен ни одному из заданных чисел.</p>";
}
}
?>
</body>
</html>