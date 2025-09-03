<?php
session_start(); 

$totalScore = $_SESSION['page1_score'] + $_SESSION['page2_score'] + $_SESSION['page3_score'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результаты тестирования</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <h1>Результаты тестирования</h1>
    <div class="result">
        Ваш результат: <?php echo $totalScore; ?> баллов.
    </div>
</body>
</html>