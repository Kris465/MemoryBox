<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Календарь месяца</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Календарь месяца</h1>
        <form method="POST" action="">
            <label for="month">Введите название месяца:</label>
            <input type="text" id="month" name="month" required>
            <input type="submit" value="Показать календарь">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $month = ucfirst(strtolower(trim($_POST['month'])));
            $months = [
                'Январь' => 1,
                'Февраль' => 2,
                'Март' => 3,
                'Апрель' => 4,
                'Май' => 5,
                'Июнь' => 6,
                'Июль' => 7,
                'Август' => 8,
                'Сентябрь' => 9,
                'Октябрь' => 10,
                'Ноябрь' => 11,
                'Декабрь' => 12
            ];

            if (array_key_exists($month, $months)) {
                $year = date("Y");
                $monthNumber = $months[$month];
                $daysInMonth = cal_days_in_month(CAL_GREGORIAN, $monthNumber, $year);
                
                echo "<h2>Календарь на $month $year</h2>";
                echo "<table>";
                echo "<tr><th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th class='weekend'>Сб</th><th class='weekend'>Вс</th></tr>";
                
                // Определяем первый день месяца
                $firstDayOfMonth = mktime(0, 0, 0, $monthNumber, 1, $year);
                $firstDayOfWeek = date('N', $firstDayOfMonth); // 1 (понедельник) - 7 (воскресенье)

                // Печатаем пустые ячейки до первого дня месяца
                echo "<tr>";
                for ($i = 1; $i < $firstDayOfWeek; $i++) {
                    echo "<td></td>";
                }

                // Печатаем дни месяца
                for ($day = 1; $day <= $daysInMonth; $day++) {
                    if (($day + $firstDayOfWeek - 1) % 7 == 0 && $day != 1) {
                        echo "</tr><tr>";
                    }
                    if (($day + $firstDayOfWeek - 1) % 7 == 6 || ($day + $firstDayOfWeek - 1) % 7 == 0) {
                        echo "<td class='weekend'>$day</td>"; // Выходные дни
                    } else {
                        echo "<td>$day</td>";
                    }
                }

                echo "</tr>";
                echo "</table>";
            } else {
                echo "<p class='error'>Неверное название месяца. Пожалуйста, введите корректное название.</p>";
            }
        }
        ?>
    </div>
</body>
</html>