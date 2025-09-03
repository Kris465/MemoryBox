<?php
session_start(); 

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['page1'])) {
        $_SESSION['page1_answers'] = $_POST['answers'];
        $_SESSION['page1_score'] = calculateScore($_POST['answers'], 1);
        header("Location: page2.php"); 
        exit();
    } elseif (isset($_POST['page2'])) {

        $_SESSION['page2_answers'] = $_POST['answers'];
        $_SESSION['page2_score'] = calculateScore($_POST['answers'], 3); 
        header("Location: page3.php");
        exit();
    } elseif (isset($_POST['page3'])) {

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
    <title>Тестирование - Страница 1</title>
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
    <h1>Страница 1: Вопросы с одним правильным ответом</h1>
    <form method="POST" action="">
        <?php for ($i = 1; $i <= 10; $i++): ?>
            <div class="question">
                <p>Вопрос <?php echo $i; ?>: Какой ответ правильный?</p>
                <label>
                    <input type="radio" name="answers[<?php echo $i; ?>]" value="correct"> Правильный ответ
                </label>
                <label>
                    <input type="radio" name="answers[<?php echo $i; ?>]" value="wrong1"> Неправильный ответ 1
                </label>
                <label>
                    <input type="radio" name="answers[<?php echo $i; ?>]" value="wrong2"> Неправильный ответ 2
                </label>
            </div>
        <?php endfor; ?>
        <button type="submit" name="page1">Next</button>
    </form>
</body>
</html>