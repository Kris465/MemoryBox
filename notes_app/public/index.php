<?php
spl_autoload_register(function ($class) {
    $file = __DIR__ . '/../app/' . str_replace('\\', '/', $class) . '.php';
    if (file_exists($file)) {
        require $file;
    }
});

$controller = new \controllers\NoteController();

$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$method = $_SERVER['REQUEST_METHOD'];

switch (true) {
    // Просмотр одной заметки (GET /show?id=123)
    case str_contains($path, '/show'):
        $id = $_GET['id'] ?? null;
        $controller->show($id);
        break;
        
    // Создание заметки
    case $path === '/create' && $method === 'GET':
        $controller->create(); // Показ формы
        break;
    case $path === '/create' && $method === 'POST':
        $controller->create(); // Обработка формы
        break;
        
    // Редактирование заметки
    case str_contains($path, '/edit') && $method === 'GET':
        $id = $_GET['id'] ?? null;
        $controller->edit($id); // Показ формы
        break;
    case str_contains($path, '/edit') && $method === 'POST':
        $id = $_GET['id'] ?? null;
        $controller->edit($id); // Обработка формы
        break;
        
    // Удаление заметки
    case str_contains($path, '/delete'):
        $id = $_GET['id'] ?? null;
        $controller->delete($id);
        break;
        
    // Главная страница
    default:
        $controller->index();
}