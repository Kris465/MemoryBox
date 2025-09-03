<?php
$visits = isset($_COOKIE['page2_visits']) ? (int)$_COOKIE['page2_visits'] + 1 : 1;
setcookie('page2_visits', $visits, time() + 3600 * 24 * 30);
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Страница 2</title>
</head>
<body>
    <h1>Это Страница 2</h1>
    <p>Вы посетили эту страницу <?php echo $visits; ?> раз(а).</p>
    <a href="index.php">Вернуться на главную</a>
</body>
</html>