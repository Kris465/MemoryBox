<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Ввод переменных</title>
</head>
<body>
    <form method="post">
        <label>Введите значение для t: <input type="number" name="t" required></label><br>
        <label>Введите значение для v: <input type="number" name="v" required></label><br>
        <label>Введите значение для x: <input type="number" name="x" required></label><br>
        <label>Введите значение для y: <input type="number" name="y" required></label><br>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        $t = intval(trim($_POST['t']));
        $v = intval(trim($_POST['v']));
        $x = intval(trim($_POST['x']));
        $y = intval(trim($_POST['y']));

        
        echo "$x $t<br>";
        echo "$v см<br>";
        echo "$x 25<br>";
        echo "$x $y<br>";
    }
    ?>
</body>
</html>