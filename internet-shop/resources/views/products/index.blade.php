@extends('layouts.app')

@section('content')
    <h1>Каталог товаров</h1>
    <div class="row">
        @foreach($products as $product)
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="{{ asset($product->image) }}" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">{{ $product->name }}</h5>
                        <p class="card-text">{{ $product->description }}</p>
                        <p class="card-text">{{ $product->price }} руб.</p>
                        <form action="{{ route('add.to.cart', $product->id) }}" method="POST">
                            @csrf
                            <button type="submit" class="btn btn-primary">В корзину</button>
                        </form>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
    <a href="{{ route('cart') }}" class="btn btn-success">Корзина</a>
    <a href="{{ route('feedback') }}" class="btn btn-info">Обратная связь</a>
@endsection