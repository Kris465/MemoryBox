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
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$number = $_POST['number'];
if (!preg_match('/^-?\d{3}$/', $number)) {
    echo "<p>Пожалуйста, введите трехзначное число.</p>";
} else {
    $abs_str = ltrim((string)$number, '-');

    if (strpos($abs_str, '4') !== false || strpos($abs_str, '7') !== false) {
        echo "<p>В числе есть цифра 4 или 7.</p>";
    } else {
        echo "<p>В числе нет цифр 4 и 7.</p>";
    }

    if (strpos($abs_str, '3') !== false || strpos($abs_str, '6') !== false || strpos($abs_str, '9') !== false) {
        echo "<p>В числе есть цифра 3, 6 или 9.</p>";
    } else {
        echo "<p>В числе нет цифр 3, 6 и 9.</p>";
    }
}
}
?>
</body>
</html>