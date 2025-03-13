<?php
$number = '';
$digits = [];
$count = 0;
$maxDigit = null;
$minDigit = null;
$sum = 0;
$average = 0;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $number = $_POST['number'];
    if (ctype_digit($number)) {

        $digits = str_split($number);

        $count = count($digits);

        $maxDigit = max($digits);
        $minDigit = min($digits);

        $sum = array_sum($digits);

        $average = $sum / $count;
    } else {
        echo "Ошибка: введены нечисловые символы.";
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Анализ числа</title>
</head>
<body>
    <h1>Анализ числа</h1>
    <form method="POST" action="">
        <label for="number">Введите число:</label>
        <input type="text" id="number" name="number" required value="<?php echo htmlspecialchars($number); ?>">
        <button type="submit">Анализировать</button>
    </form>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST' && ctype_digit($number)): ?>
        <h2>Результаты:</h2>
        <ul>
            <li>Число: <?php echo htmlspecialchars($number); ?></li>
            <li>Цифры: <?php echo implode(', ', $digits); ?></li>
            <li>Количество цифр: <?php echo $count; ?></li>
            <li>Самая большая цифра: <?php echo $maxDigit; ?></li>
            <li>Самая маленькая цифра: <?php echo $minDigit; ?></li>
            <li>Сумма цифр: <?php echo $sum; ?></li>
            <li>Среднее значение: <?php echo number_format($average, 2); ?></li>
        </ul>
    <?php endif; ?>
</body>
</html>