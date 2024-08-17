<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Нечетные числа</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="container">
    <h1>Введите количество нечетных чисел (N)</h1>
    <form method="post">
        <input type="number" name="n" min="1" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $N = (int)$_POST['n'];
        
        // Массив для хранения нечетных чисел
        $oddNumbers = [];
        
        // Генерация нечетных чисел
        for ($i = 0, $num = 1; $i < $N; $i++, $num += 2) {
            $oddNumbers[] = $num;
        }

        // Подсчет среднего значения
        $average = array_sum($oddNumbers) / count($oddNumbers);
        
        // Вывод нечетных чисел в обратном порядке
        $oddNumbersReversed = array_reverse($oddNumbers);

        // Вывод результатов
        echo "<h2>Нечетные числа: " . implode(", ", $oddNumbers) . "</h2>";
        echo "<h2>Среднее значение: " . $average . "</h2>";
        echo "<h2>Нечетные числа в обратном порядке: " . implode(", ", $oddNumbersReversed) . "</h2>";
    }
    ?>
</div>

</body>
</html>
