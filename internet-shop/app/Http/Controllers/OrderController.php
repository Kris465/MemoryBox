<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Order;

class OrderController extends Controller
{
    public function store(Request $request)
    {
        $cart = session()->get('cart');
        $total = array_sum(array_map(function($item) {
            return $item['price'] * $item['quantity'];
        }, $cart));

        $order = Order::create([
            'customer_name' => $request->name,
            'customer_email' => $request->email,
            'customer_comment' => $request->comment,
            'total_price' => $total,
        ]);

        session()->forget('cart');
        return redirect()->route('home')->with('success', 'Заказ оформлен!');
    }
}
