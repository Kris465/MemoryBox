<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мини-викторина</title>
    <link rel="stylesheet" href="styles.css"> <!-- Подключаем файл стилей -->
</head>
<body>

<?php
// Проверяем, была ли отправлена форма
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $score = 0;

    // Вопрос 1 (правильный ответ - "html")
    if (isset($_POST['q1']) && $_POST['q1'] === 'html') {
        $score++;
    }

    // Вопрос 2 (правильные ответы - "java", "ruby")
    $correctAnswersQ2 = ['java', 'ruby'];
    $userAnswersQ2 = isset($_POST['q2']) ? $_POST['q2'] : [];
    foreach ($correctAnswersQ2 as $answer) {
        if (in_array($answer, $userAnswersQ2)) {
            $score++;
        }
    }

    // Вопрос 3 (развернутый ответ)
    if (!empty(trim($_POST['q3']))) {
        $score++; // Учитываем ответ на третий вопрос
    }

    // Отображаем результат
    echo "<div class='result'>Вы набрали $score из 3 баллов.</div>";
} else {
    // Включаем шаблон формы
    include 'form.html';
}
?>

</body>
</html>
