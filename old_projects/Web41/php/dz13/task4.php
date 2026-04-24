<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .category {
            margin-bottom: 20px;
        }
        .filters {
            margin-left: 20px;
        }
    </style>
</head>
<body>

<?php

class Category {
    protected $filters = [];

    public function __construct() {}

    public function getFilters() {
        return $this->filters;
    }
}

class PhoneCategory extends Category {
    public function __construct() {
        parent::__construct();
        $this->filters[] = 'Ram';
        $this->filters[] = 'CountSim';
        $this->filters[] = 'Hdd';
        $this->filters[] = 'OS';
    }
}

class MonitorCategory extends Category {
    public function __construct() {
        parent::__construct();
        $this->filters[] = 'Diagonal';
        $this->filters[] = 'Frequency';
    }
}

$products = [
    ['name' => 'iPhone 13', 'type' => 'Phone'],
    ['name' => 'Samsung Galaxy S21', 'type' => 'Phone'],
    ['name' => 'LG UltraFine', 'type' => 'Monitor'],
    ['name' => 'Dell P2720DC', 'type' => 'Monitor'],
];

$listProducts = [];

foreach ($products as $product) {
    if ($product['type'] === 'Phone') {
        $listProducts[] = [
            'product' => $product,
            'category' => new PhoneCategory()
        ];
    } elseif ($product['type'] === 'Monitor') {
        $listProducts[] = [
            'product' => $product,
            'category' => new MonitorCategory()
        ];
    }
}

$categories = [];

foreach ($listProducts as $item) {
    $categories[$item['product']['type']][] = [
        'name' => $item['product']['name'],
        'filters' => $item['category']->getFilters()
    ];
}

foreach ($categories as $type => $items) {
    echo "<div class='category'>";
    echo "<h2>Category: " . htmlspecialchars($type) . "</h2>";
    
    foreach ($items as $item) {
        echo "<p><strong>Product:</strong> " . htmlspecialchars($item['name']) . "</p>";
        
        echo "<div class='filters'><strong>Filters:</strong><ul>";
        
        foreach ($item['filters'] as $filter) {
            echo "<li>" . htmlspecialchars($filter) . "</li>";
        }
        
        echo "</ul></div>";
        
        echo "<hr>";
    }
    
    echo "</div>";
}
?>

</body>
</html>