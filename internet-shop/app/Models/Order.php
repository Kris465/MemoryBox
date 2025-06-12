<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Order extends Model
{
    use HasFactory;

    /**
     * Поля, доступные для массового присваивания
     * 
     * @var array
     */
    protected $fillable = [
        'customer_name',
        'customer_email',
        'customer_phone', // если есть такое поле
        'customer_comment',
        'total_price',
        'status', // если есть статус заказа
        'delivery_address' // если есть адрес доставки
    ];

    /**
     * Поля, которые должны быть скрыты при сериализации
     * 
     * @var array
     */
    protected $hidden = [
        'created_at',
        'updated_at'
    ];
}