<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка цифр в двузначном числе</title>
</head>
<body>
<h2>Проверка цифр в двузначном числе</h2>
<form method="post">
Введите двузначное число: <input type="number" name="number" required><br><br>
Цифра для проверки (а): <input type="text" maxlength="1" name="a_digit" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$number = $_POST['number'];
$a_digit = $_POST['a_digit'];
if (!preg_match('/^-?\d{2}$/', $number)) {
    echo "<p>Пожалуйста, введите двузначное число.</p>";
} else {
    $abs_str = ltrim((string)$number, '-');
    if (strpos($abs_str, '3') !== false) {
        echo "<p>Цифра 3 входит в число.</p>";
    } else {
        echo "<p>Цифра 3 не входит в число.</p>";
    }
    if (strpos($abs_str, $a_digit) !== false) {
        echo "<p>Цифра {$a_digit} входит в число.</p>";
    } else {
        echo "<p>Цифра {$a_digit} не входит в число.</p>";
    }
}
}
?>
</body>
</html>