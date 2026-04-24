<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Форма ввода пользователя</title>
</head>
<body>

<?php if ($user): ?>
    <h2>Данные пользователя</h2>
    <p><?php echo $user->getUser(); ?></p>
    <hr>
    <a href="">Ввести заново</a>
<?php else: ?>
    <h2>Введите свои данные</h2>
    <form method="post" action="">
        <label for="name">Имя:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <input type="submit" value="Отправить">
    </form>
    

<?php endif;
include 'user.php';

?>

</body>
</html>