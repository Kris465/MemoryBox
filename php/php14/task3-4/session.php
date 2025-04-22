<?php
session_start();

$name = htmlspecialchars($_GET['name'] ?? 'Неизвестный пользователь');
$email = htmlspecialchars($_GET['email'] ?? 'email@example.com');

$allPurchases = [
    'ivan@example.com' => [
        ['date' => '2023-10-15', 'sessionId' => 'sess12345'],
        ['date' => '2023-11-20', 'sessionId' => 'sess54321']
    ],
    'maria@example.com' => [
        ['date' => '2023-09-05', 'sessionId' => 'sess98765']
    ],
    'elena@example.com' => [
        ['date' => '2023-12-01', 'sessionId' => 'sess13579'],
        ['date' => '2023-12-15', 'sessionId' => 'sess24680'],
        ['date' => '2024-01-10', 'sessionId' => 'sess36912']
    ],
    'dmitry@example.com' => [
        ['date' => '2023-08-22', 'sessionId' => 'sess56789']
    ]
];

$userPurchases = $allPurchases[$email] ?? [];
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>История покупок</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .user-info { background: #f0f0f0; padding: 15px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #f5f5f5; }
        .no-purchases { color: #666; font-style: italic; }
    </style>
</head>
<body>
    <div class="user-info">
        <h2>Пользователь: <?= $name ?></h2>
        <p>Email: <?= $email ?></p>
    </div>

    <h3>История покупок:</h3>
    <?php if (!empty($userPurchases)): ?>
        <table>
            <thead>
                <tr>
                    <th>Дата</th>
                    <th>ID сессии</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($userPurchases as $purchase): ?>
                    <tr>
                        <td><?= htmlspecialchars($purchase['date']) ?></td>
                        <td><?= htmlspecialchars($purchase['sessionId']) ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php else: ?>
        <p class="no-purchases">У пользователя нет истории покупок.</p>
    <?php endif; ?>
        <p><a href="index.html">Вернуться к списку пользователей</a></p>
    
    <?php
    $_SESSION['current_user'] = [
        'name' => $name,
        'email' => $email,
        'last_visit' => date('Y-m-d H:i:s')
    ];
    ?>
</body>
</html>