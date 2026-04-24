<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Количество дней в месяце</title>
</head>
<body>

<h2>Введите номер месяца</h2>
<form method="post">
    <label for="month">Номер месяца (1-12):</label>
    <input type="number" id="month" name="month" min="1" max="12" required>
    <input type="submit" value="Узнать количество дней">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['month'])) {
    $month = intval($_POST['month']);

    $year = date("Y");

    if ($month >= 1 && $month <= 12) {
        $daysInMonth = cal_days_in_month(CAL_GREGORIAN, $month, $year);
        echo "<p>В месяце $month $year года $daysInMonth дней.</p>";
    } else {
        echo "<p>Введите корректный номер месяца (от 1 до 12).</p>";
    }
}
?>

</body>
</html>