<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Цифры до числа</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="container">
    <h1>Введите число</h1>
    <form method="post">
        <input type="number" name="number" min="1" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Проверяем, что значение является числом и больше 0
        if (!isset($_POST['number']) || !is_numeric($_POST['number']) || $_POST['number'] < 1) {
            echo "<h2 style='color: red;'>Ошибка: Введите корректное положительное число.</h2>";
        } else {
            $number = (int)htmlspecialchars($_POST['number']);

            // Массив для хранения результатов
            $mirrorNumbers = [];
            $evenNumbers = [];
            $oddNumbers = [];
            $decreasingNumbers = [];

            // Функция для проверки убывающей последовательности
            function isDecreasing($num) {
                for ($j = 0; $j < strlen($num) - 1; $j++) {
                    if ($num[$j] <= $num[$j + 1]) {
                        return false;
                    }
                }
                return true;
            }

            // Проверяем числа от 1 до введенного числа
            for ($i = 1; $i < $number; $i++) {
                // Преобразуем число в строку для проверки
                $strNum = (string)$i;
                $reversedNum = strrev($strNum);

                // Проверка на зеркальное число (исключаем однозначные)
                if (strlen($strNum) > 1 && $strNum === $reversedNum) {
                    $mirrorNumbers[] = $i;
                }

                // Проверка на четность и нечетность
                if ($i % 2 === 0) {
                    $evenNumbers[] = $i;
                } else {
                    $oddNumbers[] = $i;
                }

                // Проверка на убывание (исключаем однозначные)
                if (strlen($strNum) > 1 && isDecreasing($strNum)) {
                    $decreasingNumbers[] = $i;
                }
            }

            // Вывод результатов
            echo "<h2>Зеркальные числа: " . (!empty($mirrorNumbers) ? implode(", ", $mirrorNumbers) : "Нет") . "</h2>";
            echo "<h2>Четные числа: " . (!empty($evenNumbers) ? implode(", ", $evenNumbers) : "Нет") . "</h2>";
            echo "<h2>Нечетные числа: " . (!empty($oddNumbers) ? implode(", ", $oddNumbers) : "Нет") . "</h2>";
            echo "<h2>Числа с убывающими цифрами: " . (!empty($decreasingNumbers) ? implode(", ", $decreasingNumbers) : "Нет") . "</h2>";
        }
    }
    ?>

</div>

</body>
</html>
