<?php
session_start();

if (!isset($_SESSION['categories'])) {
    $_SESSION['categories'] = [];
}

if (!isset($_SESSION['products'])) {
    $_SESSION['products'] = ['Product 1', 'Product 2', 'Product 3']; 
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['category_name'])) {
    $categoryName = trim($_POST['category_name']);
    
    if (!empty($categoryName)) {

        $_SESSION['categories'][] = $categoryName;

        $_SESSION['products'] = [];
    }
}

function findCategory($categories, $name) {
    foreach ($categories as $category) {
        if (strcasecmp($category, $name) === 0) { 
            return $category;
        }
    }
    return null; 
}

$searchResult = null;
if (isset($_POST['search_name'])) {
    $searchResult = findCategory($_SESSION['categories'], trim($_POST['search_name']));
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

<h2>Поиск категории</h2>
<form method="post" action="">
    <input type="text" name="search_name" placeholder="Название для поиска" required>
    <button type="submit">Поиск</button>
</form>

<?php if ($searchResult !== null): ?>
    <h3>Результат поиска: Категория "<?php echo htmlspecialchars($searchResult); ?>" найдена.</h3>
<?php else: ?>
    <?php if (isset($_POST['search_name'])): ?>
        <h3>Категория не найдена.</h3>
    <?php endif; ?>
<?php endif; ?>

</body>
</html>