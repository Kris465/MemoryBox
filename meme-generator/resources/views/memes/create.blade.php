@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Создать новый мем</h1>

    {{-- Flash-сообщения --}}
    @if (session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif

    @if (session('error'))
        <div class="alert alert-danger">{{ session('error') }}</div>
    @endif

    {{-- Ошибки валидации --}}
    @if ($errors->any())
        <div class="alert alert-danger">
            <ul class="mb-0">
                @foreach ($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form method="POST" action="{{ route('memes.store') }}" enctype="multipart/form-data" id="memeForm">
        @csrf

        <div class="mb-3">
            <label class="form-label">Верхний текст</label>
            <input type="text" class="form-control" name="top_text" value="{{ old('top_text') }}">
        </div>

        <div class="mb-3">
            <label class="form-label">Нижний текст</label>
            <input type="text" class="form-control" name="bottom_text" value="{{ old('bottom_text') }}">
        </div>

        <div class="mb-3">
            <label class="form-label">Изображение</label>
            <input type="file" class="form-control @error('image') is-invalid @enderror" name="image" required accept="image/*">
            @error('image')
                <div class="invalid-feedback">{{ $message }}</div>
            @enderror
        </div>

        <button type="submit" class="btn btn-primary">Создать</button>
        <a href="{{ route('memes.index') }}" class="btn btn-secondary ms-2">Назад</a>
    </form>
</div>
@endsection
