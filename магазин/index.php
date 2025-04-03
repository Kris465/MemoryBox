<?php
session_start();

if (isset($_GET['clear_session'])) {
    session_unset();
    session_destroy();
    session_start();
    $_SESSION['categories'] = [new Category('Без категории')];
    header("Location: ".str_replace('?clear_session=1', '', $_SERVER['REQUEST_URI']));
    exit();
}

if (!isset($_SESSION['categories'])) {
    $_SESSION['categories'] = [new Category('Без категории')];
} else {
    $hasDefault = false;
    foreach ($_SESSION['categories'] as $cat) {
        if ($cat->name === 'Без категории') {
            $hasDefault = true;
            break;
        }
    }
    if (!$hasDefault) {
        array_unshift($_SESSION['categories'], new Category('Без категории'));
    }
}

class Category {
    public $name;
    public $list_products;
    public $fields; 
    
    public function __construct(string $_name, array $_list_products = [], array $_fields = []) {
        $this->name = $_name;
        $this->list_products = $_list_products;
        $this->fields = $_fields;
    }
}

function displayProductCard(string $name, string $image, float $price, string $category = '', array $categoryFields = []): string {
    $name = htmlspecialchars(trim($name));
    $image = htmlspecialchars(trim($image));
    $category = htmlspecialchars(trim($category));
    $formattedPrice = number_format($price, 2, '.', ' ');
    
    $fieldsHtml = '';
    if (!empty($categoryFields)) {
        $fieldsHtml = '<div class="product-fields"><ul>';
        foreach ($categoryFields as $fieldName => $fieldValue) {
            if (!empty($fieldValue)) {
                $fieldsHtml .= '<li><strong>'.htmlspecialchars($fieldName).':</strong> '.htmlspecialchars($fieldValue).'</li>';
            }
        }
        $fieldsHtml .= '</ul></div>';
    }
    
    return <<<HTML
    <div class="product-card">
        <div class="product-image">
            <img src="{$image}" alt="{$name}" onerror="this.src='https://via.placeholder.com/300?text=No+Image'">
        </div>
        <div class="product-info">
            <h3>{$name}</h3>
            <div class="product-meta">
                <span class="product-category">{$category}</span>
                <span class="product-price">{$formattedPrice} ₽</span>
            </div>
            {$fieldsHtml}
            <div class="product-actions">
                <form method="POST" class="add-to-cart-form">
                    <input type="hidden" name="product_name" value="{$name}">
                    <input type="hidden" name="product_image" value="{$image}">
                    <input type="hidden" name="product_price" value="{$price}">
                    <input type="hidden" name="product_category" value="{$category}">
                    <button type="submit" name="add_to_cart" class="buy-button">В корзину</button>
                </form>
                <form method="POST" class="remove-product-form" onsubmit="return confirm('Вы уверены, что хотите удалить этот продукт?');">
                    <input type="hidden" name="product_name" value="{$name}">
                    <input type="hidden" name="product_category" value="{$category}">
                    <button type="submit" name="remove_product" class="remove-product-button">Удалить</button>
                </form>
            </div>
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
                'category' => $product['category'] ?? '',
                'count' => $product['quantity'] ?? 1,
                'total_price' => $product['price'] * ($product['quantity'] ?? 1)
            ];
        }
    }
    
    return array_values($cart);
}
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['remove_product'])) {
    $productName = $_POST['product_name'] ?? '';
    
    if (!empty($productName)) {
        $removed = false;
        
        // Удаляем из общего списка продуктов
        if (isset($_SESSION['products'])) {
            foreach ($_SESSION['products'] as $key => $product) {
                if ($product['name'] === $productName) {
                    unset($_SESSION['products'][$key]);
                    $removed = true;
                    break;
                }
            }
            $_SESSION['products'] = array_values($_SESSION['products']);
        }
        
        // Удаляем из всех категорий
        if (isset($_SESSION['categories'])) {
            foreach ($_SESSION['categories'] as $category) {
                if ($category !== null && isset($category->list_products)) {
                    foreach ($category->list_products as $key => $product) {
                        if ($product['name'] === $productName) {
                            unset($category->list_products[$key]);
                            $removed = true;
                        }
                    }
                    // Переиндексация только если list_products существует
                    if (isset($category->list_products)) {
                        $category->list_products = array_values($category->list_products);
                    }
                }
            }
        }
        
        if ($removed) {
            $_SESSION['success'] = "Продукт '{$productName}' успешно удален";
        } else {
            $_SESSION['error'] = "Продукт '{$productName}' не найден";
        }
    }
    
    header("Location: ".$_SERVER['PHP_SELF']."?tab=catalog");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_product'])) {
    $productName = $_POST['product_name'] ?? '';
    $productImage = $_POST['product_image'] ?? '';
    $productPrice = (float)str_replace(',', '.', $_POST['product_price'] ?? 0);
    $productCategory = $_POST['product_category'] ?? '';
    
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
            'price' => $productPrice,
            'category' => $productCategory,
            'category_fields' => $_POST['category_fields'] ?? []
        ];
        
        $categoryFields = [];
        $selectedCategory = null;
        foreach ($_SESSION['categories'] as $cat) {
            if ($cat->name === $productCategory) {
                $selectedCategory = $cat;
                break;
            }
        }
        
        if ($selectedCategory && !empty($selectedCategory->fields)) {
            foreach ($selectedCategory->fields as $field) {
                $fieldName = $field['name'];
                if (empty($_POST['category_fields'][$fieldName])) {
                    $_SESSION['error'] = "Заполните все обязательные поля для категории";
                    header("Location: ".$_SERVER['PHP_SELF']."?tab=add");
                    exit();
                }
                $categoryFields[$fieldName] = $_POST['category_fields'][$fieldName];
            }
        }
        
        $newProduct = [
            'name' => $productName,
            'image' => $productImage,
            'price' => $productPrice,
            'category' => $productCategory,
            'category_fields' => $categoryFields
        ];

        $_SESSION['products'][] = $newProduct;

        foreach ($_SESSION['categories'] as $category) {
            if ($category->name === $productCategory) {
                $category->list_products[] = $newProduct;
                break;
            }
        }
        
        $_SESSION['success'] = "Продукт '{$productName}' успешно добавлен";
    }
    header("Location: ".$_SERVER['PHP_SELF']."?tab=add");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_category'])) {
    $categoryName = trim($_POST['category_name'] ?? '');
    $fields = [];
    
    foreach ($_POST['field_name'] as $index => $fieldName) {
        $fieldName = trim($fieldName);
        if (!empty($fieldName)) {
            $fields[] = [
                'name' => $fieldName,
                'type' => $_POST['field_type'][$index] ?? 'text'
            ];
        }
    }
    
    if (empty($categoryName)) {
        $_SESSION['error'] = "Название категории не может быть пустым";
    } elseif (empty($fields)) {
        $_SESSION['error'] = "Добавьте хотя бы одно поле для категории";
    } else {
        $categoryExists = false;
        foreach ($_SESSION['categories'] as $category) {
            if (strtolower($category->name) === strtolower($categoryName)) {
                $categoryExists = true;
                break;
            }
        }
        
        if ($categoryExists) {
            $_SESSION['error'] = "Категория '{$categoryName}' уже существует";
        } else {
            $_SESSION['categories'][] = new Category($categoryName, [], $fields);
            $_SESSION['success'] = "Категория '{$categoryName}' успешно создана";
        }
    }
    
    header("Location: ".$_SERVER['PHP_SELF']."?tab=categories");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_to_cart'])) {
    $product = [
        'name' => $_POST['product_name'] ?? '',
        'image' => $_POST['product_image'] ?? '',
        'price' => (float)$_POST['product_price'] ?? 0,
        'category' => $_POST['product_category'] ?? '',
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
$_SESSION['categories'] = $_SESSION['categories'] ?? [new Category('Без категории')];

foreach ($_SESSION['categories'] as $category) {
    if ($category !== null && !isset($category->list_products)) {
        $category->list_products = [];
    }
}

$processedCart = processCart($_SESSION['cart']);
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог продуктов с категориями</title>
    <link rel="stylesheet" href="css/style.css">
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
            <button class="tab-btn <?= (isset($_GET['tab']) && $_GET['tab'] === 'categories') ? 'active' : '' ?>" 
                    onclick="window.location.href='?tab=categories'">Категории</button>
        </div>
        <div class="tab-content <?= (!isset($_GET['tab']) || $_GET['tab'] === 'catalog') ? 'active' : '' ?>" id="catalog">
            <h2>Наши продукты</h2>
            <?php if (!empty($_SESSION['categories'])): ?>
                <?php foreach ($_SESSION['categories'] as $category): ?>
                    <?php if (!empty($category->list_products)): ?>
                        <div class="category-section">
                            <h3 class="category-title"><?= htmlspecialchars($category->name) ?></h3>
                            <div class="products-grid">
                            <?php foreach ($category->list_products as $product): ?>
                                <?= displayProductCard(
                                    $product['name'], 
                                    $product['image'], 
                                    $product['price'],
                                    $category->name,
                                    $product['category_fields'] ?? []
                                ) ?>
                            <?php endforeach; ?>
                            </div>
                        </div>
                    <?php endif; ?>
                <?php endforeach; ?>
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
                                    <div class="cart-item-category"><?= htmlspecialchars($item['category']) ?></div>
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
                
                <div class="form-group">
                    <label for="product_category">Категория:</label>
                    <select id="product_category" name="product_category" required onchange="showCategoryFields(this)">
                        <option value="">-- Выберите категорию --</option>
                        <?php foreach ($_SESSION['categories'] as $category): ?>
                            <option value="<?= htmlspecialchars($category->name) ?>">
                                <?= htmlspecialchars($category->name) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>

                <div id="categoryFieldsContainer"></div>
                
                <button type="submit" name="add_product" class="submit-btn">Добавить продукт</button>
            </form>
        </div>
        
        <div class="tab-content <?= (isset($_GET['tab']) && $_GET['tab'] === 'categories') ? 'active' : '' ?>" id="categories">
            <h2>Управление категориями</h2>
            <div class="category-form">
                <h3>Добавить новую категорию</h3>
                <form method="POST" id="categoryForm">
                    <div class="form-group">
                        <label for="category_name">Название категории:</label>
                        <input type="text" id="category_name" name="category_name" required class="form-control">
                    </div>
                    <div class="form-group">
                        <label>Поля категории:</label>
                        <div id="fieldsContainer">
                            <div class="field-row">
                                <input type="text" name="field_name[]" placeholder="Название поля" class="form-control field-name">
                                <select name="field_type[]" class="form-control field-type">
                                    <option value="text">Текст</option>
                                    <option value="number">Число</option>
                                    <option value="textarea">Текст (многострочный)</option>
                                </select>
                                <button type="button" class="btn btn-remove-field" style="display:none;">×</button>
                            </div>
                        </div>
                        <button type="button" id="addFieldBtn" class="btn btn-secondary">+ Добавить поле</button>
                    </div>
                    <button type="submit" name="add_category" class="submit-btn">Создать категорию</button>
                </form>
            </div>

            <div class="category-list">
                <h3>Список категорий</h3>
                <?php if (!empty($_SESSION['categories']) && is_array($_SESSION['categories'])): ?>
                    <?php foreach ($_SESSION['categories'] as $index => $category): ?>
                        <?php if ($category !== null): ?>
                            <div class="category-item">
                                <div>
                                    <div class="category-name"><?= htmlspecialchars($category->name) ?></div>
                                    <?php if (!empty($category->fields)): ?>
                                        <div class="category-fields">
                                            <small>Поля: 
                                                <?php foreach ($category->fields as $field): ?>
                                                    <span class="field-badge"><?= htmlspecialchars($field['name']) ?> 
                                                        <em>(<?= $field['type'] ?>)</em>
                                                    </span>
                                                <?php endforeach; ?>
                                            </small>
                                        </div>
                                    <?php endif; ?>
                                    <div class="category-product-count">
                                        Товаров: <?= isset($category->list_products) ? count($category->list_products) : 0 ?>
                                    </div>
                                </div>
                                <?php if ($category->name !== 'Без категории'): ?>
                                    <div class="category-actions">
                                        <form method="POST">
                                            <input type="hidden" name="category_index" value="<?= $index ?>">
                                            <button type="submit" name="remove_category" class="remove-btn">Удалить</button>
                                        </form>
                                    </div>
                                <?php endif; ?>
                            </div>
                        <?php endif; ?>
                    <?php endforeach; ?>
                <?php else: ?>
                    <div class="empty-category">
                        <p>Нет созданных категорий</p>
                    </div>
                <?php endif; ?>
            </div>
        </div>
        <a href="?clear_session=1" class="btn btn-danger">Сбросить ВСЕ данные (debug)</a>
    </div>

    <script src="js/script.js"></script>