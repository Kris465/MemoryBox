<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\MemeController;

Route::get('/memes', [MemeController::class, 'index'])->name('memes.index');

Route::get('/memes/create', [MemeController::class, 'create'])->name('memes.create');

Route::post('/memes', [MemeController::class, 'store'])->name('memes.store');

Route::get('/memes/{meme}', [MemeController::class, 'show'])->name('memes.show');

?>