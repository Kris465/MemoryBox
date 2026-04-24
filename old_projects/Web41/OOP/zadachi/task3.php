<?php
class Product {
   public $title;
   public $price;

   public function render() {
    return "
    <div class='product'>
    <h3>$this->title</h3>
    <p>Цена: $this->price</p> 
    </div>
    ";

   }
}

$product = new Product();
$product->title = "ноутбук";
$product->price = 50000;
echo $product->render();

