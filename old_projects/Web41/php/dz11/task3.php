<?php
session_start();

// Инициализация массива категорий и продуктов
if (!isset($_SESSION['categories'])) {
    $_SESSION['categories'] = [];
}

if (!isset($_SESSION['products'])) {
    $_SESSION['products'] = ['Product 1', 'Product 2', 'Product 3']; // Пример продуктов
}

// Обработка формы добавления категории
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['category_name'])) {
    $categoryName = trim($_POST['category_name']);
    
    if (!empty($categoryName)) {
        // Добавление новой категории в массив
        $_SESSION['categories'][] = $categoryName;

        // Перемещение всех продуктов в новую категорию
        // Здесь можно добавить логику для хранения продуктов в категории

        // Очистка списка продуктов
        $_SESSION['products'] = [];
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Категории и Продукты</title>
</head>
<body>

<h1>Добавить категорию</h1>
<form method="post" action="">
    <input type="text" name="category_name" placeholder="Название категории" required>
    <button type="submit">Add</button>
</form>

<h2>Список категорий:</h2>
<ul>
    <?php foreach ($_SESSION['categories'] as $category): ?>
        <li><?php echo htmlspecialchars($category); ?></li>
    <?php endforeach; ?>
</ul>

<h2>Список продуктов:</h2>
<ul>
    <?php foreach ($_SESSION['products'] as $product): ?>
        <li><?php echo htmlspecialchars($product); ?></li>
    <?php endforeach; ?>
</ul>

</body>
</html>