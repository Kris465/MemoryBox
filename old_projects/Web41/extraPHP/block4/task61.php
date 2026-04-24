<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка на палиндромность числа</title>
</head>
<body>
<h2>Проверка, является ли число палиндромом</h2>
<form method="post">
Введите натуральное число n (до 9999): <input type="number" name="n" min="0" max="9999" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$n = $_POST['n'];
if (!preg_match('/^\d{1,4}$/', $n)) {
    echo "<p>Пожалуйста, введите число от 0 до 9999.</p>";
} else {
    $str = str_pad($n, 4, '0', STR_PAD_LEFT);
    if ($str === strrev($str)) {
        echo "<p>Число {$str} является палиндромом.</p>";
    } else {
        echo "<p>Число {$str} не является палиндромом.</p>";
    }
}
}
?>
</body>
</html>