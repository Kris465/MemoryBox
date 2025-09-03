@extends('layouts.app')

@section('content')
    <h1>Корзина</h1>
    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif
    <table class="table">
        <thead>
            <tr>
                <th>Товар</th>
                <th>Количество</th>
                <th>Цена</th>
            </tr>
        </thead>
        <tbody>
            @foreach($cart as $id => $item)
                <tr>
                    <td>{{ $item['name'] }}</td>
                    <td>{{ $item['quantity'] }}</td>
                    <td>{{ $item['price'] * $item['quantity'] }} руб.</td>
                </tr>
            @endforeach
        </tbody>
    </table>
    <form action="{{ route('checkout') }}" method="POST">
        @csrf
        <div class="mb-3">
            <label>Имя</label>
            <input type="text" name="name" class="form-control" required>
        </div>
        <div class="mb-3">
            <label>Email</label>
            <input type="email" name="email" class="form-control" required>
        </div>
        <div class="mb-3">
            <label>Комментарий</label>
            <textarea name="comment" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-success">Оформить заказ</button>
    </form>
@endsection