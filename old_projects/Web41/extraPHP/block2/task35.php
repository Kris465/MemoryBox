<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Сумма двузначных чисел</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 400px; margin: 0 auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input { width: 100%; padding: 8px; margin-bottom: 15px; box-sizing: border-box; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #45a049; }
        .result { margin-top: 20px; padding: 10px; background: #f8f8f8; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>Вычисление цифр суммы двузначных чисел</h1>
    
    <form method="post">
        <h3>Первое число:</h3>
        <label for="a1">Десятки:</label>
        <input type="number" id="a1" name="a1" min="1" max="9" required>
        
        <label for="a2">Единицы:</label>
        <input type="number" id="a2" name="a2" min="0" max="9" required>
        
        <h3>Второе число:</h3>
        <label for="b1">Десятки:</label>
        <input type="number" id="b1" name="b1" min="1" max="9" required>
        
        <label for="b2">Единицы:</label>
        <input type="number" id="b2" name="b2" min="0" max="9" required>
        
        <button type="submit">Вычислить</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
        $a1 = (int)$_POST['a1'];
        $a2 = (int)$_POST['a2'];
        $b1 = (int)$_POST['b1'];
        $b2 = (int)$_POST['b2'];
        
       
        $num1 = $a1 * 10 + $a2;
        $num2 = $b1 * 10 + $b2;
        $sum = $num1 + $num2;
        
      
        $result_tens = (int)($sum / 10);
        $result_units = $sum % 10;
        
    
        echo "<div class='result'>";
        echo "<h3>Результат:</h3>";
        echo "Первое число: $a1$a2<br>";
        echo "Второе число: $b1$b2<br>";
        echo "Сумма: $sum<br>";
        echo "Цифры суммы: <strong>десятки - $result_tens, единицы - $result_units</strong>";
        echo "</div>";
    }