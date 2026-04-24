<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сумма и произведение цифр четырехзначного числа</title>
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

            
            $sum = 0;
            $product = 1;

            
            for ($i = 0; $i < strlen($numberStr); $i++) {
                $digit = (int)$numberStr[$i];
                $sum += $digit;               
                $product *= $digit;           
            }

            echo "<h2>Результаты:</h2>";
            echo "Сумма цифр: " . htmlspecialchars($sum) . "<br>";
            echo "Произведение цифр: " . htmlspecialchars($product) . "<br>";
        } else {
            echo "Ошибка: Введите корректное четырехзначное число.<br>";
        }
    }
    ?>

    
</body>
</html>