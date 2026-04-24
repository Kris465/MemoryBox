<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Запрос возвраста</title>
</head>
<body>
    <h1>Введите возвраст</h1>
    <form method="POST" action="">
        <label for="data">возвраст:</label>
        <input type="text" id="data" name="data" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $data = htmlspecialchars($_POST['data']); 
        echo "<h2>Вы ввели: '$data'</h2>"; 
    }
    ?>

</body>
</html>