<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Meme extends Model
{
    use HasFactory;

    protected $fillable = ['top_text', 'bottom_text', 'image_data', 'mime_type'];

    // Добавьте каст для автоматической сериализации

}