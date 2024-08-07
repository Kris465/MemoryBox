<?php
$filename = 'users.txt';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Проверяем, существует ли файл
    if (!file_exists($filename)) {
        file_put_contents($filename, "");
    }

    // Читаем пользователей из файла
    $users = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    
    // Проверяем, зарегистрирован ли пользователь
    if (in_array($name, $users)) {
        echo "Рады снова вас видеть, $name!";
    } else {
        // Добавляем нового пользователя в файл
        file_put_contents($filename, $name . PHP_EOL, FILE_APPEND);
        echo "Добро пожаловать, $name!";
    }
}
?>
