<?php
$dbName = 'novels.db';

try {
    $db = new PDO("sqlite:$dbName");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $createTableQuery = "
    CREATE TABLE IF NOT EXISTS novels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        url TEXT NOT NULL UNIQUE,
        last_updated DATETIME DAFAULT CURRENT_TIMESTAMP
    );";

    $db->exec($createTableQuery);
    echo "База данных и таблица успешно созданы!";
} catch (PDOException $e) {
    echo "Ошибка: " . $e->getMessage();
}

$db = null;
?>