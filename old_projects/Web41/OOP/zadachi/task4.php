<?php
class Product {
    public static $count = 0;

    public function __construct() {

        self::$count++;
    }
}

new Product();
new Product();
echo Product::$count;
