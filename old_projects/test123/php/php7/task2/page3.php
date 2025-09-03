<?php
session_start(); 

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['page3'])) {
        $_SESSION['page3_answers'] = $_POST['answers'];
        $_SESSION['page3_score'] = calculateScore($_POST['answers'], 5); 
        header("Location: result.php"); 
        exit();
    }
}

function calculateScore($answers, $pointsPerAnswer) {
    $score = 0;
    foreach ($answers as $answer) {
        if ($answer === 'correct') { 
            $score += $pointsPerAnswer;
        }
    }
    return $score;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тестирование - Страница 3</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .question {
            margin-bottom: 20px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Страница 3: Вопросы с текстовым ответом</h1>
    <form method="POST" action="">
        <?php for ($i = 1; $i <= 10; $i++): ?>
            <div class="question">
                <p>Вопрос <?php echo $i; ?>: Введите правильный ответ:</p>
                <input type="text" name="answers[<?php echo $i; ?>]" required>
            </div>
        <?php endfor; ?>
        <button type="submit" name="page3">Finish</button>
    </form>
</body>
</html>