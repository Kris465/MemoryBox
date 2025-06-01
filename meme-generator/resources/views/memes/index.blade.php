@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1>Все мемы</h1>
            <a href="{{ route('memes.create') }}" class="btn btn-primary">Создать новый</a>
        </div>
        
        @if($memes->isEmpty())
            <div class="alert alert-info">
                Пока нет ни одного мема. <a href="{{ route('memes.create') }}">Создайте первый!</a>
            </div>
        @else
            <div class="row">
                @foreach($memes as $meme)
                    <div class="col-md-4 mb-4">
                        <div class="card h-100">
                            <img src="data:{{ $meme->mime_type }};base64,{{ base64_encode($meme->image_data) }}" 
                                class="card-img-top" 
                                alt="Мем"
                                style="height: 200px; object-fit: cover;">
                            <div class="card-body d-flex flex-column">
                                @if($meme->top_text)
                                    <h5 class="card-title">{{ $meme->top_text }}</h5>
                                @endif
                                @if($meme->bottom_text)
                                    <p class="card-text">{{ $meme->bottom_text }}</p>
                                @endif
                                <div class="mt-auto">
                                    <a href="{{ route('memes.show', $meme) }}" class="btn btn-sm btn-outline-primary">Подробнее</a>
                                </div>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>
        @endif
    </div>
@endsection