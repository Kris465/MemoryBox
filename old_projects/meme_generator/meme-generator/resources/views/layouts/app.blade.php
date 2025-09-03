<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Генератор мемов</title>
    <!-- Исправленная ссылка на Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{{ url('/') }}">Генератор мемов</a>
            <div class="navbar-nav">
                <a class="nav-link" href="{{ route('memes.index') }}">Все мемы</a>
                <a class="nav-link" href="{{ route('memes.create') }}">Создать мем</a>
            </div>
        </div>
    </nav>

    <div id="app">
        <main class="container py-4">
            @yield('content')
        </main>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>