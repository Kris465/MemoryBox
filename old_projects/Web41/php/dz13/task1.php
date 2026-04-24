<?php

class Category {
    private $name;
    private $filters = array();
    private $listProducts = array();

    public function __construct($name, $filters = array()) {
        $this->name = $name;
        
        $this->filters = array_merge($filters, ["Price"]);
    }

    public function getName() {
        return $this->name;
    }

    public function getFilters() {
        return $this->filters;
    }

    public function getListProducts() {
        return $this->listProducts;
    }

    public function addProduct($product) {
        array_push($this->listProducts, $product);
    }
}


$category = new Category("Electronics", ["Brand", "Color"]);
echo "Category Name: " . $category->getName() . "\n";
echo "Filters: " . implode(", ", $category->getFilters()) . "\n";
?>