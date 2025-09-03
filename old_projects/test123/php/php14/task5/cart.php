<?php
session_start();

$allCarts = [
    'sess12345' => [
        ['product' => 'iPhone 13', 'price' => 799, 'quantity' => 1],
        ['product' => 'AirPods Pro', 'price' => 249, 'quantity' => 2]
    ],
    'sess54321' => [
        ['product' => 'MacBook Pro', 'price' => 1999, 'quantity' => 1]
    ],
    'sess98765' => [
        ['product' => 'iPad Air', 'price' => 599, 'quantity' => 1],
        ['product' => 'Apple Pencil', 'price' => 129, 'quantity' => 1]
    ],
    'sess13579' => [
        ['product' => 'Apple Watch', 'price' => 399, 'quantity' => 1]
    ],
    'sess24680' => [
        ['product' => 'HomePod mini', 'price' => 99, 'quantity' => 3]
    ],
    'sess36912' => [
        ['product' => 'iPhone Charger', 'price' => 19, 'quantity' => 2],
        ['product' => 'AirTag', 'price' => 29, 'quantity' => 4]
    ],
    'sess56789' => [
        ['product' => 'Mac mini', 'price' => 699, 'quantity' => 1],
        ['product' => 'Magic Keyboard', 'price' => 99, 'quantity' => 1],
        ['product' => 'Magic Mouse', 'price' => 79, 'quantity' => 1]
    ]
];

$sessionId = htmlspecialchars($_GET['sessionId'] ?? '');
$email = htmlspecialchars($_GET['email'] ?? '');

$cartItems = $allCarts[$sessionId] ?? [];
$total = 0;
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Корзина покупок</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .cart-info { background: #f0f8ff; padding: 15px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #f5f5f5; }
        .total { font-weight: bold; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="cart-info">
        <h2>Корзина покупок</h2>
        <p>ID сессии: <?= $sessionId ?></p>
        <p>Пользователь: <?= $email ?></p>
    </div>

    <h3>Товары в корзине:</h3>
    <?php if (!empty($cartItems)): ?>
        <table>
            <thead>
                <tr>
                    <th>Товар</th>
                    <th>Цена</th>
                    <th>Количество</th>
                    <th>Сумма</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($cartItems as $item): 
                    $sum = $item['price'] * $item['quantity'];
                    $total += $sum;
                ?>
                    <tr>
                        <td><?= htmlspecialchars($item['product']) ?></td>
                        <td>$<?= number_format($item['price'], 2) ?></td>
                        <td><?= $item['quantity'] ?></td>
                        <td>$<?= number_format($sum, 2) ?></td>
                    </tr>
                <?php endforeach; ?>
                <tr class="total">
                    <td colspan="3">Итого:</td>
                    <td>$<?= number_format($total, 2) ?></td>
                </tr>
            </tbody>
        </table>
    <?php else: ?>
        <p>Корзина для данной сессии пуста.</p>
    <?php endif; ?>

    <p><a href="sessions.php?email=<?= urlencode($email) ?>">Вернуться к истории покупок</a></p>
</body>
</html>