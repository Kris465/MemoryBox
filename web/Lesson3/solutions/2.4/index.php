<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Високосный год</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <form method="POST" onsubmit="return validateYear()">
            <label for="year">Введите год:</label>
            <input type="number" id="year" name="year" required>
            <button type="submit">Проверить</button>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $year = intval($_POST['year']);
            if (($year % 4 == 0 && $year % 100 != 0) || ($year % 400 == 0)) {
                echo "<p>$year - високосный год.</p>";
            } else {
                echo "<p>$year - не високосный год.</p>";
            }
        }
        ?>
    </div>
    <script src="script.js"></script>
</body>
</html>
