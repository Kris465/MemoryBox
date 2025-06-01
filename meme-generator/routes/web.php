<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\MemeController;

Route::get('/', [MemeController::class, 'index']);
Route::resource('memes', MemeController::class);

?>