<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if (!isset($_COOKIE['page1_visits'])) {
    setcookie('page1_visits', 0, time() + 3600 * 24 * 30); 
}
if (!isset($_COOKIE['page2_visits'])) {
    setcookie('page2_visits', 0, time() + 3600 * 24 * 30);
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Главная страница</title>
</head>
<body>
    <h1>Добро пожаловать на главную страницу!</h1>
    
    <nav>
        <ul>
            <li><a href="1.php">Страница 1</a></li>
            <li><a href="2.php">Страница 2</a></li>
        </ul>
    </nav>
    
    <h2>Статистика переходов:</h2>
    <p>Переходов на Страницу 1: <?php echo $_COOKIE['page1_visits'] ?? 0; ?></p>
    <p>Переходов на Страницу 2: <?php echo $_COOKIE['page2_visits'] ?? 0; ?></p>
</body>
</html>