<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\FeedbackController;
use App\Http\Controllers\OrderController;
use App\Http\Controllers\ProductController;

Route::get('/', [ProductController::class, 'index'])->name('home');
Route::get('/cart', [ProductController::class, 'cart'])->name('cart');
Route::post('/add-to-cart/{id}', [ProductController::class, 'addToCart'])->name('add.to.cart');
Route::post('/checkout', [OrderController::class, 'store'])->name('checkout');
Route::get('/feedback', [FeedbackController::class, 'show'])->name('feedback');
Route::post('/feedback', [FeedbackController::class, 'send'])->name('feedback.send');
