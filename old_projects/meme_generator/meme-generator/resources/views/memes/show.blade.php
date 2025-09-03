@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="card">
            <img src="{{ $imageSrc }}" class="card-img-top" alt="Meme">
            <div class="card-body text-center">
                @if($meme->top_text)
                    <h2 class="card-title">{{ $meme->top_text }}</h2>
                @endif
                @if($meme->bottom_text)
                    <h2 class="card-text">{{ $meme->bottom_text }}</h2>
                @endif
            </div>
        </div>
        <a href="{{ route('memes.index') }}" class="btn btn-secondary mt-3">Назад</a>
    </div>
@endsection