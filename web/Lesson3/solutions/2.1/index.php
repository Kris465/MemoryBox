<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Проверка кратности</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
        }
        .container {
            width: 300px;
            margin: 50px auto;
            padding: 20px;
            border: 2px solid #008cba;
            border-radius: 10px;
            background-color: #ffffff;
            text-align: center;
        }
        input {
            margin: 10px 0;
            padding: 10px;
            width: calc(100% - 22px);
        }
        button {
            padding: 10px 15px;
            background-color: #008cba;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #005f7f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Проверка кратности</h1>
        <form method="post" action="">
            <input type="number" name="firstNumber" placeholder="Введите первое число" required>
            <input type="number" name="secondNumber" placeholder="Введите второе число" required>
            <button type="submit">Проверить</button>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $firstNumber = intval($_POST['firstNumber']);
            $secondNumber = intval($_POST['secondNumber']);
            
            if ($secondNumber === 0) {
                echo "<p>На ноль делить нельзя!</p>";
            } elseif ($firstNumber % $secondNumber === 0) {
                echo "<p>$firstNumber кратно $secondNumber.</p>";
            } else {
                echo "<p>$firstNumber не кратно $secondNumber.</p>";
            }
        }
        ?>
    </div>
</body>
</html>
