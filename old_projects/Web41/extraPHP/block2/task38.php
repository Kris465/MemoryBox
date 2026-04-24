<!DOCTYPE html>
<html>
<head>
    <title>Определение k-й цифры в последовательности</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 400px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input { width: 100px; padding: 8px; margin-bottom: 15px; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; background: #f0f0f0; border-radius: 5px; }
        .case { margin-top: 10px; padding: 10px; background: #e9e9e9; border-radius: 3px; }
    </style>
</head>
<body>
    <h2>Определение k-й цифры в последовательности от 101 до 150</h2>
    <form method="post">
        <label for="k">Введите число k (1 ≤ k ≤ 150):</label>
        <input type="number" id="k" name="k" min="1" max="150" required>
        <button type="submit">Вычислить</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $k = (int)$_POST['k'];
        
        if ($k < 1 || $k > 150) {
            echo "<div class='result'>Ошибка: k должно быть от 1 до 150</div>";
            exit;
        }

        $number_index = (int)(($k - 1) / 3) + 1;

        $three_digit_number = 100 + $number_index;

        $digit_position = ($k - 1) % 3;
        
        switch ($digit_position) {
            case 0: $digit = (int)($three_digit_number / 100); break;
            case 1: $digit = (int)(($three_digit_number % 100) / 10); break;
            case 2: $digit = $three_digit_number % 10; break;
        }
        
        echo "<div class='result'>";
        echo "<h3>Результаты для k = $k:</h3>";
        echo "<p>Номер трехзначного числа: <strong>$number_index</strong></p>";
        echo "<p>Трехзначное число: <strong>$three_digit_number</strong></p>";
        
        echo "<div class='case'>";
        echo "<h4>Определение цифры:</h4>";
        if ($k % 3 == 0) {
            echo "<p>k кратно 3 → последняя цифра числа: <strong>$digit</strong></p>";
        } elseif (($k - 1) % 3 == 0) {
            echo "<p>k в последовательности 1,4,7,... → первая цифра числа: <strong>$digit</strong></p>";
        } else {
            echo "<p>k в последовательности 2,5,8,... → вторая цифра числа: <strong>$digit</strong></p>";
        }
        echo "</div>";
        
        echo "<p>$k-я цифра в последовательности: <strong>$digit</strong></p>";
        echo "</div>";
    }
    ?>
</body>
</html>