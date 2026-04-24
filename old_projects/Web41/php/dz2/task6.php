<?php

session_start();


if (!isset($_SESSION['session_id'])) {
    $_SESSION['session_id'] = 0; 
}

if ($_SESSION['session_id'] == 0) {

    ?>
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Регистрация</title>
    </head>
    <body>

    <h2>Форма регистрации</h2>
    <form method="post" action="">
        <label for="username">Логин:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Пароль:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Зарегистрироваться">
    </form>

    <?php

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {

        $username = $_POST['username'];
        $password = $_POST['password'];


        $_SESSION['session_id'] = 1;


        header("Location: " . $_SERVER['PHP_SELF']);
        exit();
    }

    ?>
    </body>
    </html>
    <?php
} else {

    echo "<p>Вы зарегистрированы, войдите.</p>";
}
?>