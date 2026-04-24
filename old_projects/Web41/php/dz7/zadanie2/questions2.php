<?php
session_start(); // Инициализация сессии

// Вопросы и ответы
$questions2 = [
    "Вопрос 1: Какие из этих языков являются языками программирования? (Выберите все подходящие)" => [
        "PHP", "HTML", "CSS", "Python"
    ],
    "Вопрос 2: Какие из этих технологий используются для веб-разработки? (Выберите все подходящие)" => [
        "JavaScript", "Photoshop", "Node.js", "C++"
    ],
    "Вопрос 3: Какие из этих языков являются функциональными? (Выберите все подходящие)" => [
        "Haskell", "Java", "C", "Scala"
    ],
    "Вопрос 4: Какие из этих языков используются для анализа данных? (Выберите все подходящие)" => [
        "Python", "R", "Java", "C#"
    ],
    "Вопрос 5: Какие из этих языков являются языками разметки? (Выберите все подходящие)" => [
        "HTML", "XML", "CSS", "JSON"
    ],
    "Вопрос 6: Какие из этих технологий используются для создания мобильных приложений? (Выберите все подходящие)" => [
        "Swift", "Java", "HTML", "C#"
    ],
    "Вопрос 7: Какие из этих языков являются языками стилей? (Выберите все подходящие)" => [
        "CSS", "SASS", "LESS", "HTML"
    ],
    "Вопрос 8: Какие из этих языков используются для серверной разработки? (Выберите все подходящие)" => [
        "PHP", "Ruby", "Java", "HTML"
    ],
    "Вопрос 9: Какие из этих языков являются языками разметки? (Выберите все подходящие)" => [
        "HTML", "Markdown", "XML", "CSS"
    ],
    "Вопрос 10: Какие из этих языков используются для создания игр? (Выберите все подходящие)" => [
        "C++", "C#", "Java", "Python"
    ],
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $score = 0;
    $correctAnswers = [
        ['PHP', 'Python'],
        ['JavaScript', 'Node.js'],
        ['Haskell', 'Scala'],
        ['Python', 'R'],
        ['HTML', 'XML'],
        ['Swift', 'Java', 'C#'],
        ['CSS', 'SASS', 'LESS'],
        ['PHP', 'Ruby', 'Java'],
        ['HTML', 'XML'],
        ['C++', 'C#', 'Java']
    ]; 

    foreach ($correctAnswers as $index => $answers) {
        if (isset($_POST['question' . $index])) {
            $userAnswers = $_POST['question' . $index];
            if (array_diff($answers, $userAnswers) === [] && count($userAnswers) === count($answers)) {
                $score += 3; 
            }
        }
    }
    $_SESSION['score2'] = $score2; 
    header('Location: questions3.php'); 
    exit();
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тест - Вопросы 2</title>
</head>
<body>
    <form method="POST">
        <?php foreach ($questions2 as $question => $answers): ?>
            <p><?php echo $question; ?></p>
            <?php foreach ($answers as $answer): ?>
                <label>
                    <input type="checkbox" name="question<?php echo array_search($question, array_keys($questions2)); ?>[]" value="<?php echo $answer; ?>">
                    <?php echo $answer; ?>
                </label><br>
            <?php endforeach; ?>
        <?php endforeach; ?>
        <button type="submit">Next</button>
    </form>
</body>
</html>