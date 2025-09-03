<?php

namespace App\Http\Controllers;

use App\Models\Meme;
use Illuminate\Http\Request;

class MemeController extends Controller 
{
        public function index()
    {
        $memes = Meme::latest()->get();
        return view('memes.index', compact('memes'));
    }


    public function create()
    {
        return view('memes.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'top_text' => 'nullable|string|max:255',
            'bottom_text' => 'nullable|string|max:255',
            'image' => 'required|image|mimes:jpeg,png,jpg,gif,webp|max:2048',
        ]);

        try {
            // Получаем файл
            $image = $request->file('image');
            
            // Проверяем, что файл был загружен
            if (!$image->isValid()) {
                throw new \Exception('Файл не был загружен');
            }

            // Сохраняем в БД как BLOB
            $meme = new Meme();
            $meme->top_text = $validated['top_text'];
            $meme->bottom_text = $validated['bottom_text'];
            $meme->image_data = file_get_contents($image->getRealPath());
            $meme->mime_type = $image->getClientMimeType();
            $meme->save();

            return redirect()->route('memes.show', $meme)->with('success', 'Мем создан!');

        } catch (\Exception $e) {
            return back()->withInput()->with('error', 'Ошибка: '.$e->getMessage());
        }
    }

    public function show(Meme $meme)
    {
        if (!$meme->image_data) {
            abort(404, 'Изображение не найдено');
        }

        return view('memes.show', [
            'meme' => $meme,
            'imageSrc' => 'data:'.$meme->mime_type.';base64,'.base64_encode($meme->image_data)
        ]);
    }
}