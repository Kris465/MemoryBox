<?php
session_start(); 

class Category {
    private $name;
    private $list_products = array();

    public function __construct($name, $products = array()) {
        $this->name = $name;
        $this->list_products = $products;
    }

    public function getCategoryName() {
        return $this->name;
    }

    public function getCategoryProducts() {
        return $this->list_products;
    }

    public function addProduct($product) {
        array_push($this->list_products, $product);
    }

    public static function findCategory($categories, $name) {
        foreach ($categories as $category) {
            if ($category->getCategoryName() == $name) {
                return $category;
            }
        }
        return null;
    }
}


$categories = isset($_SESSION['categories']) ? $_SESSION['categories'] : array();

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['add_category'])) {
    $name = trim($_POST['category_name']);
    
    if (!empty($name)) {
        $existingCategory = Category::findCategory($categories, $name);
        
        if ($existingCategory === null) {
            $newCategory = new Category($name);
            array_push($categories, $newCategory);

            $_SESSION['categories'] = $categories;

            if (isset($_SESSION['products'])) {
                unset($_SESSION['products']);
            }
        }
    }

    header("Location: ".$_SERVER['PHP_SELF']);
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Category Manager</title>
</head>
<body>
    <h1>Category Management</h1>

    <form method="POST" action="">
        <label for="category_name">Category Name:</label>
        <input type="text" id="category_name" name="category_name" required>
        <button type="submit" name="add_category">Add Category</button>
    </form>

    <h2>Categories:</h2>
    <ul>
        <?php foreach ($categories as $category): ?>
            <li>
                <?= htmlspecialchars($category->getCategoryName()) ?>
                (Products: <?= count($category->getCategoryProducts()) ?>)
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>