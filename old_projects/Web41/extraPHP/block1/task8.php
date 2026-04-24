<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Ввод чисел</title>
</head>
<body>
    <form method="post">
        <label>Введите первое число: <input type="text" name="first"></label><br>
        <label>Введите второе число: <input type="text" name="second"></label><br>
        <label>Введите третье число: <input type="text" name="third"></label><br>
        <label>Введите четвертое число: <input type="text" name="fourth"></label><br>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
 
        $first = trim($_POST['first']);
        $second = trim($_POST['second']);
        $third = trim($_POST['third']);
        $fourth = trim($_POST['fourth']);

        echo "$first $second $third $fourth";
    }
    ?>
</body>
</html>