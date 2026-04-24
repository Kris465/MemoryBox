<?php
session_start();

function displayProductCard(string $name, string $image, float $price): string {
    $name = htmlspecialchars(trim($name));
    $image = htmlspecialchars(trim($image));
    $formattedPrice = number_format($price, 2, '.', ' ');
    
    return <<<HTML
    <div class="product-card">
        <div class="product-image">
            <img src="{$image}" alt="{$name}" onerror="this.src='https://via.placeholder.com/300?text=No+Image'">
        </div>
        <div class="product-info">
            <h3>{$name}</h3>
            <div class="product-price">{$formattedPrice} ₽</div>
            <form method="POST">
                <input type="hidden" name="product_name" value="{$name}">
                <input type="hidden" name="product_image" value="{$image}">
                <input type="hidden" name="product_price" value="{$price}">
                <button type="submit" name="add_to_cart" class="buy-button">В корзину</button>
            </form>
        </div>
    </div>
HTML;
}

function processCart(array $products): array {
    $cart = [];
    
    foreach ($products as $product) {
        $key = $product['name'].'|'.$product['price'];
        
        if (isset($cart[$key])) {
            $cart[$key]['count'] += $product['quantity'] ?? 1;
            $cart[$key]['total_price'] += $product['price'] * ($product['quantity'] ?? 1);
        } else {
            $cart[$key] = [
                'name' => $product['name'],
                'image' => $product['image'] ?? '',
                'price' => $product['price'],
                'count' => $product['quantity'] ?? 1,
                'total_price' => $product['price'] * ($product['quantity'] ?? 1)
            ];
        }
    }
    
    return array_values($cart);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_product'])) {
    $productName = $_POST['product_name'] ?? '';
    $productImage = $_POST['product_image'] ?? '';
    $productPrice = (float)str_replace(',', '.', $_POST['product_price'] ?? 0);
    
    if (!is_numeric($productPrice)) {
        $_SESSION['error'] = "Цена должна быть числом";
    } elseif ($productPrice <= 0) {
        $_SESSION['error'] = "Цена должна быть больше нуля";
    } elseif (empty($productName)) {
        $_SESSION['error'] = "Название продукта не может быть пустым";
    } else {
        $newProduct = [
            'name' => $productName,
            'image' => $productImage,
            'price' => $productPrice
        ];
        $_SESSION['products'][] = $newProduct;
    }
    header("Location: ".$_SERVER['PHP_SELF']);
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_to_cart'])) {
    $product = [
        'name' => $_POST['product_name'] ?? '',
        'image' => $_POST['product_image'] ?? '',
        'price' => (float)$_POST['product_price'] ?? 0,
        'quantity' => 1
    ];
    $_SESSION['cart'][] = $product;
    $_SESSION['success'] = "Товар добавлен в корзину!";
    header("Location: ".$_SERVER['PHP_SELF']."?tab=cart");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['update_quantity'])) {
    $index = $_POST['item_index'] ?? null;
    $newQuantity = (int)($_POST['quantity'] ?? 1);
    
    if ($index !== null && isset($_SESSION['cart'][$index])) {
        if ($newQuantity > 0) {
            $_SESSION['cart'][$index]['quantity'] = $newQuantity;
            $_SESSION['success'] = "Количество товара обновлено";
        } else {
            unset($_SESSION['cart'][$index]);
            $_SESSION['success'] = "Товар удален из корзины";
        }
    }
    header("Location: ".$_SERVER['PHP_SELF']."?tab=cart");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['remove_item'])) {
    $index = $_POST['item_index'] ?? null;
    if ($index !== null && isset($_SESSION['cart'][$index])) {
        unset($_SESSION['cart'][$index]);
        $_SESSION['success'] = "Товар удален из корзины";
    }
    header("Location: ".$_SERVER['PHP_SELF']."?tab=cart");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['clear_cart'])) {
    unset($_SESSION['cart']);
    $_SESSION['success'] = "Корзина очищена";
    header("Location: ".$_SERVER['PHP_SELF']."?tab=cart");
    exit();
}

$_SESSION['products'] = $_SESSION['products'] ?? [];
$_SESSION['cart'] = $_SESSION['cart'] ?? [];

$processedCart = processCart($_SESSION['cart']);
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог продуктов с корзиной</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background: #333;
            color: white;
            padding: 15px 0;
            margin-bottom: 30px;
        }
        header .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .cart-link {
            color: white;
            text-decoration: none;
            font-weight: bold;
            position: relative;
        }
        .cart-count {
            background: #ff5722;
            border-radius: 50%;
            padding: 2px 6px;
            font-size: 12px;
            position: absolute;
            top: -10px;
            right: -10px;
        }
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .product-card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .product-image img {
            width: 100%;
            height: 200px;
            object-fit: contain;
            margin: 20px 0;
        }
        .product-info {
            padding: 15px;
        }
        .product-info h3 {
            margin-top: 0;
        }
        .product-price {
            font-size: 20px;
            font-weight: bold;
            color: #e53935;
            margin: 10px 0;
        }
        .buy-button {
            background: #ff5722;
            color: white;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 4px;
            cursor: pointer;
        }
        .buy-button:hover {
            background: #e64a19;
        }
        .product-form {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"], input[type="number"] {
            padding: 10px 0 10px 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .submit-btn {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            width: 100%;
        }
        .submit-btn:hover {
            background: #45a049;
        }
        .error {
            color: #e53935;
            padding: 10px;
            background: #ffebee;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        .success {
            color: #2e7d32;
            padding: 10px;
            background: #e8f5e9;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        .cart-items {
            margin-top: 30px;
        }
        .cart-item {
            display: flex;
            align-items: center;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .cart-item-image {
            width: 80px;
            height: 80px;
            object-fit: contain;
            margin-right: 20px;
            border-radius: 4px;
        }
        .cart-item-info {
            flex-grow: 1;
        }
        .cart-item-name {
            font-weight: bold;
            margin-bottom: 5px;
        }
        .cart-item-price {
            color: #e53935;
        }
        .cart-item-quantity {
            margin: 10px 0;
        }
        .cart-item-total {
            font-weight: bold;
            margin-left: auto;
            min-width: 100px;
            text-align: right;
        }
        .cart-summary {
            margin-top: 20px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: right;
        }
        .cart-total {
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }
        .btn {
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        .btn-clear {
            background: #f44336;
            color: white;
        }
        .btn-clear:hover {
            background: #d32f2f;
        }
        .btn-checkout {
            background: #4CAF50;
            color: white;
            margin-left: 10px;
        }
        .btn-checkout:hover {
            background: #388E3C;
        }
        .empty-cart {
            text-align: center;
            padding: 40px;
            color: #777;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        .tabs {
            display: flex;
            margin-bottom: 20px;
            border-bottom: 1px solid #ddd;
        }
        .tab-btn {
            padding: 10px 20px;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-bottom: 3px solid transparent;
        }
        .tab-btn.active {
            border-bottom: 3px solid #4CAF50;
            font-weight: bold;
        }
        .quantity-controls {
            display: flex;
            align-items: center;
            margin: 10px 0;
        }
        .quantity-input {
            width: 50px;
            text-align: center;
            padding: 5px;
            margin: 0 5px;
        }
        .quantity-btn {
            background: #ddd;
            border: none;
            width: 25px;
            height: 25px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .quantity-btn:hover {
            background: #ccc;
        }
        .update-btn {
            background: #2196F3;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            margin-left: 10px;
        }
        .update-btn:hover {
            background: #0b7dda;
        }
        .remove-btn {
            background: #f44336;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            margin-left: 10px;
        }
        .remove-btn:hover {
            background: #d32f2f;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Магазин продуктов</h1>
            <a href="?tab=cart" class="cart-link">
                Корзина
                <?php if (!empty($_SESSION['cart'])): ?>
                    <span class="cart-count"><?= count($_SESSION['cart']) ?></span>
                <?php endif; ?>
            </a>
        </div>
    </header>

    <div class="container">
        <?php if (isset($_SESSION['error'])): ?>
            <div class="error"><?= htmlspecialchars($_SESSION['error']) ?></div>
            <?php unset($_SESSION['error']); ?>
        <?php endif; ?>
        
        <?php if (isset($_SESSION['success'])): ?>
            <div class="success"><?= htmlspecialchars($_SESSION['success']) ?></div>
            <?php unset($_SESSION['success']); ?>
        <?php endif; ?>

        <div class="tabs">
            <button class="tab-btn <?= (!isset($_GET['tab']) || $_GET['tab'] === 'catalog') ? 'active' : '' ?>" 
                    onclick="window.location.href='?tab=catalog'">Каталог</button>
            <button class="tab-btn <?= (isset($_GET['tab']) && $_GET['tab'] === 'cart') ? 'active' : '' ?>" 
                    onclick="window.location.href='?tab=cart'">Корзина</button>
            <button class="tab-btn <?= (isset($_GET['tab']) && $_GET['tab'] === 'add') ? 'active' : '' ?>" 
                    onclick="window.location.href='?tab=add'">Добавить продукт</button>
        </div>
        <div class="tab-content <?= (!isset($_GET['tab']) || $_GET['tab'] === 'catalog') ? 'active' : '' ?>" id="catalog">
        <h2>Наши продукты</h2>
        <?php if (!empty($_SESSION['products'])): ?>
            <div class="products-grid">
                <?php foreach ($_SESSION['products'] as $product): ?>
                    <?= displayProductCard($product['name'], $product['image'], $product['price']) ?>
                <?php endforeach; ?>
            </div>
        <?php else: ?>
            <p>Каталог пуст. Добавьте продукты через вкладку "Добавить продукт".</p>
        <?php endif; ?>
    </div>

    <div class="tab-content <?= (isset($_GET['tab']) && $_GET['tab'] === 'cart') ? 'active' : '' ?>" id="cart">
        <h2>Ваша корзина</h2>
        <?php if (!empty($processedCart)): ?>
            <form method="POST">
                <div class="cart-items">
                    <?php 
                    $grandTotal = 0;
                    foreach ($processedCart as $index => $item): 
                        $grandTotal += $item['total_price'];
                    ?>
                        <div class="cart-item">
                            <img src="<?= htmlspecialchars($item['image']) ?>" 
                                 alt="<?= htmlspecialchars($item['name']) ?>" 
                                 class="cart-item-image"
                                 onerror="this.src='https://via.placeholder.com/80?text=No+Image'">
                            <div class="cart-item-info">
                                <div class="cart-item-name"><?= htmlspecialchars($item['name']) ?></div>
                                <div class="cart-item-price"><?= number_format($item['price'], 2, '.', ' ') ?> ₽ за шт.</div>
                                <div class="quantity-controls">
                                    <button type="button" class="quantity-btn minus" data-index="<?= $index ?>">-</button>
                                    <input type="number" name="quantity[<?= $index ?>]" 
                                           value="<?= $item['count'] ?>" min="1" 
                                           class="quantity-input" id="quantity-<?= $index ?>">
                                    <button type="button" class="quantity-btn plus" data-index="<?= $index ?>">+</button>
                                    <input type="hidden" name="item_index" value="<?= $index ?>">
                                    <button type="submit" name="update_quantity" class="update-btn">Обновить</button>
                                    <button type="submit" name="remove_item" class="remove-btn">Удалить</button>
                                </div>
                            </div>
                            <div class="cart-item-total">
                                <?= number_format($item['total_price'], 2, '.', ' ') ?> ₽
                            </div>
                        </div>
                    <?php endforeach; ?>
                    
                    <div class="cart-summary">
                        <div class="cart-total">
                            Итого: <?= number_format($grandTotal, 2, '.', ' ') ?> ₽
                        </div>
                        <button type="submit" name="clear_cart" class="btn btn-clear">Очистить корзину</button>
                        <button type="button" class="btn btn-checkout">Оформить заказ</button>
                    </div>
                </div>
            </form>
        <?php else: ?>
            <div class="empty-cart">
                <p>Ваша корзина пуста</p>
            </div>
        <?php endif; ?>
    </div>

    <div class="tab-content <?= (isset($_GET['tab']) && $_GET['tab'] === 'add') ? 'active' : '' ?>" id="add">
        <h2>Добавить новый продукт</h2>
        <form method="POST" class="product-form">
            <div class="form-group">
                <label for="product_name">Название продукта:</label>
                <input type="text" id="product_name" name="product_name" required>
            </div>
            
            <div class="form-group">
                <label for="product_image">URL изображения:</label>
                <input type="text" id="product_image" name="product_image" placeholder="https://example.com/image.jpg">
            </div>
            
            <div class="form-group">
                <label for="product_price">Цена (руб):</label>
                <input type="text" id="product_price" name="product_price" required 
                       pattern="\d+([\.,]\d{1,2})?" 
                       title="Введите цену в формате 1234.56">
            </div>
            
            <button type="submit" name="add_product" class="submit-btn">Добавить продукт</button>
        </form>
    </div>
    <script>
        document.querySelectorAll('.quantity-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const index = this.dataset.index;
                const input = document.getElementById(`quantity-${index}`);
                let value = parseInt(input.value);
                
                if (this.classList.contains('minus')) {
                    if (value > 1) value--;
                } else if (this.classList.contains('plus')) {
                    value++;
                }
                
                input.value = value;
            });
        });
    </script>
</body>
</html>