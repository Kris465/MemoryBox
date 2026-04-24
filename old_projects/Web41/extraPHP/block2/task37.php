<!DOCTYPE html>
<html>
<head>
    <title>Определение цифр в последовательности</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 400px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input { width: 100px; padding: 8px; margin-bottom: 15px; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; background: #f0f0f0; border-radius: 5px; }
    </style>
</head>
<body>
    <h2>Определение цифр в последовательности двузначных чисел</h2>
    <form method="post">
        <label for="k">Введите число k (1 ≤ k ≤ 180):</label>
        <input type="number" id="k" name="k" min="1" max="180" required>
        <button type="submit">Вычислить</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $k = (int)$_POST['k'];
        
        if ($k < 1 || $k > 180) {
            echo "<div class='result'>Ошибка: k должно быть от 1 до 180</div>";
            exit;
        }
        
        $pair_number = (int)(($k + 1) / 2);
        
        $two_digit_number = 10 + $pair_number - 1;
        
        $digit = ($k % 2 == 1) ? (int)($two_digit_number / 10) : $two_digit_number % 10;
        
        echo "<div class='result'>";
        echo "<h3>Результаты для k = $k:</h3>";
        echo "<p>а) Номер пары цифр: <strong>$pair_number</strong></p>";
        echo "<p>б) Двузначное число: <strong>$two_digit_number</strong></p>";
        echo "<p>в) $k-я цифра: <strong>$digit</strong></p>";
        echo "</div>";
    }
    ?>
</body>
</html>