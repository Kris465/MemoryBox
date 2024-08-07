<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Квадрат большего числа</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Квадрат большего числа</h1>
        <form method="post" action="">
            <input type="number" name="firstNumber" placeholder="Введите первое число" required>
            <input type="number" name="secondNumber" placeholder="Введите второе число" required>
            <button type="submit">Посчитать</button>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $firstNumber = intval($_POST['firstNumber']);
            $secondNumber = intval($_POST['secondNumber']);
            
            $maxNumber = max($firstNumber, $secondNumber);
            $result = $maxNumber ** 2;

            echo "<p class='result'>Квадрат большего числа ($maxNumber) равен: <span>$result</span></p>";
        }
        ?>
    </div>
</body>
</html>
