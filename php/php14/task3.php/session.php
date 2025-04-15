<?php
$name = $_GET['name'] ?? 'Не указано';
$email = $_GET['email'] ?? 'Не указан';

setcookie('user_name', $name, time() + 3600, '/');
setcookie('user_email', $email, time() + 3600, '/');

session_start();
$_SESSION['user'] = [
    'name' => $name,
    'email' => $email
];

?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Информация о пользователе</title>
</head>
<body>
    <h1>Данные пользователя</h1>
    <p><strong>Имя:</strong> <?= htmlspecialchars($name) ?></p>
    <p><strong>Email:</strong> <?= htmlspecialchars($email) ?></p>
    
    <h2>Сохраненные данные:</h2>
    <p><strong>Cookie (имя):</strong> <?= $_COOKIE['user_name'] ?? 'Не установлено' ?></p>
    <p><strong>Cookie (email):</strong> <?= $_COOKIE['user_email'] ?? 'Не установлено' ?></p>
    
    <p><strong>Сессия:</strong></p>
    <pre><?php print_r($_SESSION['user'] ?? 'Не установлено'); ?></pre>
    
    <p><a href="index.html">Вернуться к списку пользователей</a></p>
</body>
</html>