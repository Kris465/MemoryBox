<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Викторина</title>
</head>
<body>
    <h1>Викторина</h1>
    <form method="POST" action="">
        <h2>a) Вопрос 1: Какой язык программирования используется для веб-разработки?</h2>
        <label><input type="radio" name="q1" value="1"> PHP</label><br>
        <label><input type="radio" name="q1" value="2"> Python</label><br>
        <label><input type="radio" name="q1" value="3"> Java</label><br>
        <label><input type="radio" name="q1" value="4"> C++</label><br>

        <h2>b) Вопрос 2: Какие из следующих языков являются языками программирования?</h2>
        <label><input type="checkbox" name="q2[]" value="1"> HTML</label><br>
        <label><input type="checkbox" name="q2[]" value="2"> JavaScript</label><br>
        <label><input type="checkbox" name="q2[]" value="3"> CSS</label><br>
        <label><input type="checkbox" name="q2[]" value="4"> Ruby</label><br>

        <h2>c) Вопрос 3: Опишите, что такое объектно-ориентированное программирование.</h2>
        <textarea name="q3" rows="4" cols="50" required></textarea><br>

        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
       
        $q1_answer = $_POST['q1'] ?? null;
        $q2_answers = $_POST['q2'] ?? [];
        $q3_answer = htmlspecialchars($_POST['q3']);

        $correct_q1 = 1; 
        $correct_q2 = [2, 4]; 

        if ($q1_answer == $correct_q1) {
            echo "<h3>Вопрос 1: Правильно!</h3>";
        } else {
            echo "<h3>Вопрос 1: Неправильно. Правильный ответ: PHP.</h3>";
        }

        $correct_q2_count = 0;
        foreach ($correct_q2 as $correct_answer) {
            if (in_array($correct_answer, $q2_answers)) {
                $correct_q2_count++;
            }
        }
        if ($correct_q2_count == count($correct_q2) && count($q2_answers) == count($correct_q2)) {
            echo "<h3>Вопрос 2: Правильно!</h3>";
        } else {
            echo "<h3>Вопрос 2: Неправильно. Правильные ответы: JavaScript, Ruby.</h3>";
        }

       
        echo "<h3>Вопрос 3: Ваш ответ:</h3>";
        echo "<p>$q3_answer</p>";
    }
    ?>
</body>
</html>