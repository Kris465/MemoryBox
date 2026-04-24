<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка цифр в трехзначном числе</title>
</head>
<body>
<h2>Проверка цифр в трехзначном числе</h2>
<form method="post">
Введите трехзначное число: <input type="number" name="number" required><br><br>
Введите цифру n для проверки: <input type="text" maxlength="1" name="n_digit" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$number = $_POST['number'];
$n_digit = $_POST['n_digit'];

if (!preg_match('/^-?\d{3}$/', $number)) {
    echo "<p>Пожалуйста, введите трехзначное число.</p>";
} else {
    $abs_str = ltrim((string)$number, '-');

    if (strpos($abs_str, '6') !== false) {
        echo "<p>Цифра 6 входит в число.</p>";
    } else {
        echo "<p>Цифра 6 не входит в число.</p>";
    }

    if (strpos($abs_str, $n_digit) !== false) {
        echo "<p>Цифра {$n_digit} входит в число.</p>";
    } else {
        echo "<p>Цифра {$n_digit} не входит в число.</p>";
    }
}
}
?>
</body>
</html>