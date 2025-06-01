<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('memes', function (Blueprint $table) {
            $table->id();
            $table->text('top_text')->nullable();
            $table->text('bottom_text')->nullable();
            $table->longText('image_data'); // Для хранения base64 или бинарных данных
            $table->string('mime_type', 50); // Для хранения типа изображения (image/jpeg и т.д.)
            $table->timestamps(); // created_at и updated_at
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('memes');
    }
};
