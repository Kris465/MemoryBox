<!DOCTYPE html>
<html>
<head>
    <title>Генератор мемов</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    <h1>Мои мемы</h1>
    <a href="{{ route('generator') }}">Создать новый</a>
    
    <div class="memes">
        @foreach($memes as $meme)
            <div class="meme">
                <img src="{{ asset($meme->image_path) }}" alt="Мем">
                <p>{{ $meme->top_text }}</p>
                <p>{{ $meme->bottom_text }}</p>
            </div>
        @endforeach
    </div>
</body>
</html>