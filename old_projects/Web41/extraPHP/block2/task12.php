<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Анализ трехзначного числа</title>
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

        function analyzeThreeDigitNumber($number) {
            
            $hundreds = (int)($number / 100); 
            $tens = (int)(($number % 100) / 10); 
            $units = (int)($number % 10); 

            
            $sum = $hundreds + $tens + $units;
            $product = $hundreds * $tens * $units;

            return [
                'units' => $units,
                'tens' => $tens,
                'sum' => $sum,
                'product' => $product,
            ];
        }

        if (is_numeric($inputNumber)) {
            $result = analyzeThreeDigitNumber((int)$inputNumber);
            
            if (is_array($result)) {
                echo "<h2>Результаты:</h2>";
                echo "Число единиц: " . htmlspecialchars($result['units']) . "<br>";
                echo "Число десятков: " . htmlspecialchars($result['tens']) . "<br>";
                echo "Сумма цифр: " . htmlspecialchars($result['sum']) . "<br>";
                echo "Произведение цифр: " . htmlspecialchars($result['product']) . "<br>";
            }
        } else {
            echo "Ошибка: Введите корректное трехзначное число.<br>";
        }
    }
    ?>
</body>
</html>