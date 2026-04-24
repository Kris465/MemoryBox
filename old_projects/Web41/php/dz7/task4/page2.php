<?php
session_start();
if (!isset($_SESSION['answers1'])) {
    header('Location: index.php');
    exit();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $_SESSION['answers2'] = $_POST;
    header('Location: page3.php');
    exit();
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тестирование - Страница 2</title>
    <style>
        .options {
            display: inline-block;
            margin-right: 10px;
        }
        .next-button {
            margin-top: 30px; /* Отступ сверху для кнопки */
        }
    </style>
</head>
<body>
    <h1>Вопросы с несколькими правильными ответами</h1>
    <form method="POST">
        <?php
        $questions = [
            "1. Вопрос 1?" => ['a', 'b', 'c', 'd'],
            "2. Вопрос 2?" => ['a', 'b', 'c', 'd'],
            "3. Вопрос 3?" => ['a', 'b', 'c', 'd'],
            "4. Вопрос 4?" => ['a', 'b', 'c', 'd'],
            "5. Вопрос 5?" => ['a', 'b', 'c', 'd'],
            "6. Вопрос 6?" => ['a', 'b', 'c', 'd'],
            "7. Вопрос 7?" => ['a', 'b', 'c', 'd'],
            "8. Вопрос 8?" => ['a', 'b', 'c', 'd'],
            "9. Вопрос 9?" => ['a', 'b', 'c', 'd'],
            "10. Вопрос 10?" => ['a', 'b', 'c', 'd'],
        ];
        
        foreach ($questions as $question => $options) {
            echo "<p>$question</p>";
            foreach ($options as $option) {
                echo "<label class='options'><input type='checkbox' name='{$question}[]' value='$option'> $option</label>";
            }
        }
        ?>
        <div class="next-button">
            <button type="submit">Next</button>
        </div>
    </form>
</body>
</html>