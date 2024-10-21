<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Количество дней в месяце</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container" id="container">
        <h1>Количество дней в месяце</h1>
        <form method="post" action="">
            <input type="text" name="month" placeholder="Введите название месяца" required>
            <button type="submit">Узнать</button>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $month = strtolower(trim($_POST['month']));
            $daysInMonth = 0;

            switch ($month) {
                case 'январь':
                case 'март':
                case 'май':
                case 'июль':
                case 'август':
                case 'октябрь':
                case 'декабрь':
                    $daysInMonth = 31;
                    break;
                case 'апрель':
                case 'июнь':
                case 'сентябрь':
                case 'ноябрь':
                    $daysInMonth = 30;
                    break;
                case 'февраль':
                    $daysInMonth = 28;
                    break;
                default:
                    echo "<p class='error'>Некорректное название месяца.</p>";
                    break;
            }

            if ($daysInMonth > 0) {
                echo "<p class='result'>В месяце $month $daysInMonth дней.</p>";
            }
        }
        ?>
    </div>
    <script src="script.js"></script>
</body>
</html>
