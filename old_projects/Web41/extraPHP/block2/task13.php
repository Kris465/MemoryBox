<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Перевернуть трехзначное число</title>
</head>
<body>
    <h1>Введите трехзначное число</h1>
    <form method="post">
        <input type="number" name="number" min="100" max="999" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $inputNumber = $_POST['number'];

        if ($inputNumber >= 100 && $inputNumber <= 999) {
            $reversedNumber = strrev((string)$inputNumber);
            
            echo "<h2>Результат:</h2>";
            echo "Число, полученное при прочтении цифр справа налево: " . htmlspecialchars($reversedNumber) . "<br>";
        } else {
            echo "Ошибка: Введите корректное трехзначное число.<br>";
        }
    }
    ?>
</body>
</html>