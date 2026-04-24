<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обработка четырехзначного числа</title>
</head>
<body>
    <h1>Введите четырехзначное число</h1>
    <form method="post">
        <input type="number" name="number" min="1000" max="9999" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $inputNumber = $_POST['number'];

        if ($inputNumber >= 1000 && $inputNumber <= 9999) {
            $numberStr = (string)$inputNumber;

            $reversedNumber = strrev($numberStr);

            $swappedNumber = $numberStr[1] . $numberStr[0] . $numberStr[3] . $numberStr[2];

            echo "<h2>Результаты:</h2>";
            echo "Число, полученное при прочтении справа налево: " . htmlspecialchars($reversedNumber) . "<br>";
            echo "Число после перестановки: " . htmlspecialchars($swappedNumber) . "<br>";
        } else {
            echo "Ошибка: Введите корректное четырехзначное число.<br>";
        }
    }
    ?>
</body>
</html>