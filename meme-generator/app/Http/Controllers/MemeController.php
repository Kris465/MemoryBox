<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Meme;
use Intervention\Image\Facades\Image;  # если будем использовать
use Illuminate\Support\Facades\Storage;

class MemeController extends Controller
{
    public function index()
    {
        $memes = Meme::latest()->get();
        return view('home', compact('memes'));
    }

    public function generator()
    {
        $defaultImages = Storage::files('public/memes/default');
        return view('generator', compact('defaultImages'));
    }

    public function generate(Request $request)
    {
        return response()->json(['memeUrl' => 'путь_к_изображению']);
    }

    public function save(Request $request)
    {
        $meme = Meme::create([
            'image_path' => $request->image_path,
            'top_text' => $request->top_text,
            'bottom_text' => $request->bottom_text,
        ]);
        return redirect()->route('home');
    }
}