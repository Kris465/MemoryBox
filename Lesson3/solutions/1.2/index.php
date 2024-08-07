<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма ввода</title>
</head>
<body>

<?php
$name = '';
$hobby = '';
$message = '';

// Проверяем, была ли форма отправлена
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Получаем данные из формы и очищаем их
    $name = htmlspecialchars($_POST['name']);
    $hobby = htmlspecialchars($_POST['hobby']);
    
    // Формируем сообщение
    $message = "Привет, $name, я тоже люблю $hobby.";
}
?>

<form method="post" action="">
    <label for="name">Введите ваше имя:</label>
    <input type="text" id="name" name="name" required>
    
    <br><br>
    
    <label for="hobby">Введите ваше хобби:</label>
    <input type="text" id="hobby" name="hobby" required>
    
    <br><br>
    
    <input type="submit" value="Отправить">
</form>

<?php if ($message): ?>
    <p><?php echo $message; ?></p>
<?php endif; ?>

</body>
</html>
