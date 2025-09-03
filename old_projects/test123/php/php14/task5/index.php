<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Список пользователей</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .user-link { display: block; margin: 10px 0; padding: 8px; background: #f0f0f0; }
    </style>
</head>
<body>
    <h1>Список пользователей</h1>
    <div id="users-container"></div>

    <script>
        class User {
            constructor(name, email, purchases = []) {
                this.name = name;
                this.email = email;
                this.purchases = purchases;
            }
            
            addPurchase(date, sessionId) {
                this.purchases.push({date, sessionId});
            }
            
            getUserInfo() {
                return `${this.name} — ${this.email}`;
            }
        }

        const users = [
            new User('Иван Иванов', 'ivan@example.com', [
                {date: '2023-10-15', sessionId: 'sess12345'},
                {date: '2023-11-20', sessionId: 'sess54321'}
            ]),
            new User('Мария Петрова', 'maria@example.com', [
                {date: '2023-09-05', sessionId: 'sess98765'}
            ]),
            new User('Алексей Сидоров', 'alex@example.com', []),
            new User('Елена Васильева', 'elena@example.com', [
                {date: '2023-12-01', sessionId: 'sess13579'},
                {date: '2023-12-15', sessionId: 'sess24680'},
                {date: '2024-01-10', sessionId: 'sess36912'}
            ]),
            new User('Дмитрий Николаев', 'dmitry@example.com', [
                {date: '2023-08-22', sessionId: 'sess56789'}
            ])
        ];

        const container = document.getElementById('users-container');
        users.forEach(user => {
            const link = document.createElement('a');
            link.href = `sessions.php?name=${encodeURIComponent(user.name)}&email=${encodeURIComponent(user.email)}`;
            link.className = 'user-link';
            link.textContent = user.getUserInfo();
            container.appendChild(link);
        });
    </script>
</body>
</html>