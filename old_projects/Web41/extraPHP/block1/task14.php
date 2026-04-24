<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Ввод числа</title>
</head>
<body>
    <form method="post">
        <label>Введите число: <input type="number" name="number" required></label>
        <br>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST['number'])) {
            $number = intval(trim($_POST['number']));
            echo "$number - вот какое число Вы ввели";
        }
    }
    ?>
</body>
</html>