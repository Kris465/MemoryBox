<?php
session_start(); // Инициализация сессии

// Вопросы и ответы
$questions1 = [
    "Вопрос 1: Какой язык программирования используется для веб-разработки?" => [
        "PHP", "Python", "JavaScript", "C++"
    ],
    "Вопрос 2: Какой протокол используется для передачи данных в интернете?" => [
        "HTTP", "FTP", "SMTP", "POP3"
    ],
    "Вопрос 3: Какой из этих языков является языком разметки?" => [
        "HTML", "CSS", "JavaScript", "PHP"
    ],
    "Вопрос 4: Какой язык программирования используется для создания мобильных приложений?" => [
        "Java", "C#", "Swift", "Ruby"
    ],
    "Вопрос 5: Какой из этих языков является языком стилей?" => [
        "CSS", "HTML", "JavaScript", "PHP"
    ],
    "Вопрос 6: Какой язык программирования используется для серверной разработки?" => [
        "PHP", "HTML", "CSS", "SQL"
    ],
    "Вопрос 7: Какой из этих языков является функциональным?" => [
        "Haskell", "Java", "C++", "Python"
    ],
    "Вопрос 8: Какой язык программирования используется для анализа данных?" => [
        "Python", "Java", "C", "Ruby"
    ],
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $score = 0;
    $correctAnswers = ['PHP', 'HTTP', 'HTML', 'Java', 'CSS', 'PHP', 'Haskell', 'Python']; // Правильные ответы
    foreach ($correctAnswers as $index => $answer) {
        if (isset($_POST['question' . $index]) && $_POST['question' . $index] === $answer) {
            $score++;
        }
    }
    $_SESSION['score1'] = $score1; // Сохраняем количество правильных ответов
    header('Location: questions2.php'); // Переход на вторую страницу
    exit();
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тест - Вопросы 1</title>
</head>
<body>
    <form method="POST">
        <?php foreach ($questions1 as $question => $answers): ?>
            <p><?php echo $question; ?></p>
            <?php foreach ($answers as $index => $answer): ?>
                <label>
                    <input type="radio" name="question<?php echo array_search($question, array_keys($questions1)); ?>" value="<?php echo $answer; ?>">
                    <?php echo $answer; ?>
                </label><br>
            <?php endforeach; ?>
        <?php endforeach; ?>
        <button type="submit">Next</button>
    </form>
</body>
</html>