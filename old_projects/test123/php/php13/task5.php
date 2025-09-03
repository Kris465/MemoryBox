<?php
$products = [
    ['name' => 'iPhone 13', 'category' => 'Phone', 'price' => 799, 'weight' => 174],
    ['name' => 'Samsung Monitor', 'category' => 'Monitor', 'price' => 299, 'size' => 27],
    ['name' => 'Pixel 7', 'category' => 'Phone', 'price' => 599, 'weight' => 197],
    ['name' => 'LG Monitor', 'category' => 'Monitor', 'price' => 199, 'size' => 24]
];

$categories = array_unique(array_column($products, 'category'));

function getMinMaxForCategory($products, $category, $field) {
    $values = [];
    foreach ($products as $product) {
        if ($product['category'] === $category && isset($product[$field])) {
            $values[] = $product[$field];
        }
    }
    return !empty($values) ? ['min' => min($values), 'max' => max($values)] : null;
}

if (isset($_GET['category'])) {
    $selectedCategory = $_GET['category'];
    $filters = [];

    if ($selectedCategory === 'Phone') {
        $filters['weight'] = getMinMaxForCategory($products, $selectedCategory, 'weight');
    } elseif ($selectedCategory === 'Monitor') {
        $filters['size'] = getMinMaxForCategory($products, $selectedCategory, 'size');
    }

    $filters['price'] = getMinMaxForCategory($products, $selectedCategory, 'price');

    foreach ($filters as $filterName => $range) {
        if ($range) {
            echo '<div class="filter">';
            echo '<label>'.ucfirst($filterName).'</label>';
            echo '<input type="text" placeholder="Min: '.$range['min'].'" name="'.$filterName.'_min">';
            echo '<input type="text" placeholder="Max: '.$range['max'].'" name="'.$filterName.'_max">';
            echo '</div>';
        }
    }
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Category Filters</title>
    <style>
        .category { cursor: pointer; margin: 5px; padding: 5px; background: #eee; }
        .filter-container { margin-top: 20px; }
        .filter { margin-bottom: 10px; }
        .filter input { margin-left: 5px; }
    </style>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('.category').click(function() {
                const category = $(this).data('category');
                $('.filter-container').html('Loading...');
                
                $.get('index.php', {category: category}, function(data) {
                    $('.filter-container').html(data);
                });
            });
        });
    </script>
</head>
<body>
    <h1>Categories</h1>
    <?php foreach ($categories as $category): ?>
        <div class="category" data-category="<?= htmlspecialchars($category) ?>">
            <?= htmlspecialchars($category) ?>
        </div>
    <?php endforeach; ?>
    
    <div class="filter-container">
    </div>
</body>
</html>