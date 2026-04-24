<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Проверка високосного года</title>
</head>
<body>

<h2>Введите год для проверки</h2>
<form method="post">
    <label for="year">Год:</label>
    <input type="number" id="year" name="year" required>
    <input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['year'])) {
    $year = intval($_POST['year']); 

    if (($year % 4 === 0 && $year % 100 !== 0) || ($year % 400 === 0)) {
        echo "<p>$year является високосным годом.</p>";
    } else {
        echo "<p>$year не является высокосным годом.</p>";
    }
}
?>

</body>
</html>