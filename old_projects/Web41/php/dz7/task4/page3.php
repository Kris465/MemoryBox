<?php
session_start();
if (!isset($_SESSION['answers2'])) {
    header('Location: page2.php');
    exit();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $_SESSION['answers3'] = $_POST;
    header('Location: result.php');
    exit();
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тестирование - Страница 3</title>
    <style>
        .next-button {
            margin-top: 30px; /* Отступ сверху для кнопки */
        }
    </style>
</head>
<body>
    <h1>Вопросы с текстовым ответом</h1>
    <form method="POST">
        <?php
        $questions = [
            "1. Вопрос 1?" => '',
            "2. Вопрос 2?" => '',
            "3. Вопрос 3?" => '',
            "4. Вопрос 4?" => '',
            "5. Вопрос 5?" => '',
            "6. Вопрос 6?" => '',
            "7. Вопрос 7?" => '',
            "8. Вопрос 8?" => '',
            "9. Вопрос 9?" => '',
            "10. Вопрос 10?" => '',
        ];
        
        foreach ($questions as $question => $value) {
            echo "<p>$question</p>";
            echo "<input type='text' name='$question'><br>";
        }
        ?>
        <div class="next-button">
            <button type="submit">Finish</button>
        </div>
    </form>
</body>
</html>