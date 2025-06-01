@extends('layouts.app')

@section('content')
    <div class="container">
        <h1>Создать новый мем</h1>
        <form id="memeForm" action="{{ route('memes.store') }}" method="POST" enctype="multipart/form-data">
            @csrf
            <div class="mb-3">
                <label class="form-label">Верхний текст</label>
                <input type="text" class="form-control" name="top_text">
            </div>
            <div class="mb-3">
                <label class="form-label">Нижний текст</label>
                <input type="text" class="form-control" name="bottom_text">
            </div>
            <div class="mb-3">
                <label class="form-label">Изображение</label>
                <input type="file" class="form-control" name="image" id="imageInput" required>
                <div class="invalid-feedback" id="imageError"></div>
            </div>
            <button type="submit" class="btn btn-primary">Создать</button>
        </form>

        <script>
        document.getElementById('memeForm').addEventListener('submit', function(e) {
            const fileInput = document.getElementById('imageInput');
            if(fileInput.files.length === 0) {
                e.preventDefault();
                document.getElementById('imageError').textContent = 'Выберите изображение';
                fileInput.classList.add('is-invalid');
            }
        });
        </script>
        <a href="{{ route('memes.index') }}" class="btn btn-secondary mt-3">Все мемы</a>
    </div>
@endsection