<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сумма трехзначного и двузначного чисел</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="number"] {
            width: 60px;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
        }
        .number-inputs {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        .number-inputs input {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Сумма трехзначного и двузначного чисел</h1>
    
    <form method="post">
        <div class="form-group">
            <label>Трехзначное число:</label>
            <div class="number-inputs">
                <input type="number" name="a1" min="1" max="9" placeholder="Сотни" required>
                <input type="number" name="a2" min="0" max="9" placeholder="Десятки" required>
                <input type="number" name="a3" min="0" max="9" placeholder="Единицы" required>
            </div>
        </div>
        
        <div class="form-group">
            <label>Двузначное число:</label>
            <div class="number-inputs">
                <input type="number" name="b1" min="1" max="9" placeholder="Десятки" required>
                <input type="number" name="b2" min="0" max="9" placeholder="Единицы" required>
            </div>
        </div>
        
        <button type="submit">Вычислить сумму</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        $a1 = (int)$_POST['a1']; 
        $a2 = (int)$_POST['a2']; 
        $a3 = (int)$_POST['a3'];
        $b1 = (int)$_POST['b1'];
        $b2 = (int)$_POST['b2']; 
        
        
        $sum = $a1*100 + $a2*10 + $a3 + $b1*10 + $b2;
        
       
        $hundreds = (int)($sum / 100);
        $tens = (int)(($sum % 100) / 10);
        $units = $sum % 10;
        
       
        echo '<div class="result">';
        echo '<h2>Результат:</h2>';
        echo '<p><strong>Цифры суммы:</strong></p>';
        echo '<p>Сотни: ' . $hundreds . '</p>';
        echo '<p>Десятки: ' . $tens . '</p>';
        echo '<p>Единицы: ' . $units . '</p>';
        echo '</div>';
    }
    ?>
</body>
</html>