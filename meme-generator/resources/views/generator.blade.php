<!DOCTYPE html>
<html>
<head>
    <title>Генератор мемов</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
    <h1>Создай свой мем</h1>
    <form id="memeForm">
        @csrf
        <input type="file" name="image" id="imageUpload">
        <input type="text" name="top_text" placeholder="Верхний текст">
        <input type="text" name="bottom_text" placeholder="Нижний текст">
        <button type="button" onclick="generateMeme()">Сгенерировать</button>
    </form>

    <div id="memeResult"></div>

    <script>
        function generateMeme() {
            const formData = new FormData(document.getElementById('memeForm'));
            
            fetch("{{ route('generate') }}", {
                method: 'POST',
                body: formData,
                headers: { 'X-CSRF-TOKEN': '{{ csrf_token() }}' }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('memeResult').innerHTML = `<img src="${data.memeUrl}">`;
            });
        }
    </script>
</body>
</html>