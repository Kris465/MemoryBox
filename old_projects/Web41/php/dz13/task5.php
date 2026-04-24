<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Categories</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .category {
            cursor: pointer;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .filters {
            display: none; /* Скрываем фильтры по умолчанию */
            margin-left: 20px;
        }
        .filter-input {
            margin-top: 5px;
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
    ['name' => 'iPhone 13', 'type' => 'Phone', 'ram' => 4, 'countSim' => 2, 'hdd' => 128, 'os' => 'iOS'],
    ['name' => 'Samsung Galaxy S21', 'type' => 'Phone', 'ram' => 8, 'countSim' => 2, 'hdd' => 256, 'os' => 'Android'],
    ['name' => 'LG UltraFine', 'type' => 'Monitor', 'diagonal' => 27, 'frequency' => 60],
    ['name' => 'Dell P2720DC', 'type' => 'Monitor', 'diagonal' => 27, 'frequency' => 75],
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
        // Добавляем значения для фильтров
        // Для телефонов
        // Для мониторов
        // Можно добавить дополнительные параметры по необходимости
        ...$item['product']
    ];
}

foreach ($categories as $type => $items) {
    echo "<div class='category' onclick='toggleFilters(\"$type\")'>";
    echo "<h2>Category: " . htmlspecialchars($type) . "</h2>";
    
    echo "<div class='filters' id='$type-filters'>";
    
    foreach ($items as $item) {
        echo "<div>";
        
        if ($type === "Phone") {
            echo "<strong>Product:</strong> " . htmlspecialchars($item['name']) . "<br>";
            echo "<label>Ram:</label> ";
            echo "<input type='text' class='filter-input' placeholder='Min: " . min(array_column($items, "ram")) . "'> - ";
            echo "<input type='text' class='filter-input' placeholder='Max: " . max(array_column($items, "ram")) . "'><br>";
            
            echo "<label>CountSim:</label> ";
            echo "<input type='text' class='filter-input' placeholder='Min: " . min(array_column($items, "countSim")) . "'> - ";
            echo "<input type='text' class='filter-input' placeholder='Max: " . max(array_column($items, "countSim")) . "'><br>";
            
            echo "<label>Hdd:</label> ";
            echo "<input type='text' class='filter-input' placeholder='Min: " . min(array_column($items, "hdd")) . "'> - ";
            echo "<input type='text' class='filter-input' placeholder='Max: " . max(array_column($items, "hdd")) . "'><br>";
            
            echo "<label>OS:</label> " . htmlspecialchars($item['os']) . "<br>";
            
        } elseif ($type === "Monitor") {
            echo "<strong>Product:</strong> " . htmlspecialchars($item['name']) . "<br>";
            echo "<label>Diagonal:</label> ";
            echo "<input type='text' class='filter-input' placeholder='Min: " . min(array_column($items, "diagonal")) . "'> - ";
            echo "<input type='text' class='filter-input' placeholder='Max: " . max(array_column($items, "diagonal")) . "'><br>";
            
            echo "<label>Frequency:</label> ";
            echo "<input type='text' class='filter-input' placeholder='Min: " . min(array_column($items, "frequency")) . "'> - ";
            echo "<input type='text' class='filter-input filter-frequency' placeholder=Max: ". max(array_column($items,"frequency"))."><br>";
            
         }

         echo "</div><hr>"; // Разделитель между продуктами
     }

     echo "</div>"; // Закрываем div с фильтрами
     echo "</div>"; // Закрываем div с категорией
 }

?>

<script>
function toggleFilters(category) {
   const filtersDiv = document.getElementById(category + '-filters');
   if (filtersDiv.style.display === '' || filtersDiv.style.display === 'none') {
       filtersDiv.style.display = 'block'; // Показываем фильтры
   } else {
       filtersDiv.style.display = ''; // Скрываем фильтры
   }
}
</script>

</body>
</html>