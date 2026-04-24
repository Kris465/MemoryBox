<?php
class Category {
    private $name;
    private $list_products = array();

    public function __construct($name, $products = array()) {
        $this->name = $name;
        $this->list_products = $products;
    }

    public function getCategoryName() {
        return $this->name;
    }

    public function getCategoryProducts() {
        return $this->list_products;
    }

    public function addProduct($product) {
        array_push($this->list_products, $product);
    }

    public static function findCategory($categories, $name) {
        foreach ($categories as $category) {
            if ($category->getCategoryName() == $name) {
                return $category;
            }
        }
        return null;
    }
}
?>
