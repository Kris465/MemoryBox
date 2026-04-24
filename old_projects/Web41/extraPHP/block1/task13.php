<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Ввод переменных</title>
</head>
<body>
    <form method="post">
        <label>Введите значение для a: <input type="number" name="a" required></label><br>
        <label>Введите значение для b: <input type="number" name="b" required></label><br>
        <label>Введите значение для x: <input type="number" name="x" required></label><br>
        <label>Введите значение для y: <input type="number" name="y" required></label><br>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        
        $a = intval(trim($_POST['a']));
        $b = intval(trim($_POST['b']));
        $x = intval(trim($_POST['x']));
        $y = intval(trim($_POST['y']));

        
        echo "$a кг<br>";
        echo "$x $y<br>";
        echo "$b 1<br>";
        echo "19 $b<br>";
        echo "$x $y<br>";
        echo "5 $y<br>";
    }
    ?>
</body>
</html>