<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма ввода имени</title>
</head>
<body>

<?php include 'process.php'; ?>

<form method="post" action="">
    <label for="name">Введите ваше имя:</label>
    <input type="text" id="name" name="name" required>
    <input type="submit" value="Отправить">
</form>

<?php if ($message): ?>
    <p><?php echo $message; ?></p>
<?php endif; ?>

</body>
</html>
