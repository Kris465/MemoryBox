<?php
session_start(); // Инициализация сессии

// Вопросы и ответы
$questions3 = [
    "Вопрос 1: Назовите язык программирования, используемый для создания веб-сайтов.",
    "Вопрос 2: Какой язык используется для создания мобильных приложений на iOS?",
    "Вопрос 3: Какой язык программирования используется для анализа данных?",
    "Вопрос 4: Назовите язык, который является языком разметки.",
    "Вопрос 5: Какой язык программирования используется для создания серверных приложений?",
    "Вопрос 6: Назовите язык, который используется для создания игр.",
    "Вопрос 7: Какой язык программирования используется для создания скриптов на стороне клиента?",
    "Вопрос 8: Назовите язык, который используется для работы с базами данных.",
    "Вопрос 9: Какой язык программирования используется для создания веб-приложений?",
    "Вопрос 10: Назовите язык, который используется для создания интерфейсов пользователя."
];

$correctAnswers = [
    "PHP",
    "Swift",
    "Python",
    "HTML",
    "Java",
    "C++",
    "JavaScript",
    "SQL",
    "Ruby",
    "Java"
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $score = 0;
    foreach ($correctAnswers as $index => $answer) {
        if (isset($_POST['question' . $index]) && strtolower(trim($_POST['question' . $index])) === strtolower($answer)) {
            $score += 5; 
        }
    }
    $_SESSION['score3'] = $score3; 
    header('Location: results.php'); 
    exit();
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тест - Вопросы 3</title>
</head>
<body>
    <form method="POST">
        <?php foreach ($questions3 as $index => $question): ?>
            <p><?php echo $question; ?></p>
            <input type="text" name="question<?php echo $index; ?>" required>
        <?php endforeach; ?>
        <button type="submit">Finish</button>
    </form>
</body>
</html>