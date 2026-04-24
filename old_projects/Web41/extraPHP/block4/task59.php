<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка цифр в четырехзначном числе</title>
</head>
<body>
<h2>Проверка цифр в четырехзначном числе</h2>
<form method="post">
Введите четырехзначное число: <input type="number" name="number" required><br><br>
Введите цифру b для проверки: <input type="text" maxlength="1" name="b_digit" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$number = $_POST['number'];
$b_digit = $_POST['b_digit'];

if (!preg_match('/^-?\d{4}$/', $number)) {
    echo "<p>Пожалуйста, введите четырехзначное число.</p>";
} else {
    $abs_str = ltrim((string)$number, '-');

    if (strpos($abs_str, '4') !== false) {
        echo "<p>Цифра 4 входит в число.</p>";
    } else {
        echo "<p>Цифра 4 не входит в число.</p>";
    }

    if (strpos($abs_str, $b_digit) !== false) {
        echo "<p>Цифра {$b_digit} входит в число.</p>";
    } else {
        echo "<p>Цифра {$b_digit} не входит в число.</p>";
    }
}
}
?>
</body>
</html>