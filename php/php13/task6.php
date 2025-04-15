<?php
$products = [
    ['name' => 'iPhone 13', 'category' => 'Phone', 'price' => 799, 'weight' => 174],
    ['name' => 'Samsung Monitor', 'category' => 'Monitor', 'price' => 299, 'size' => 27],
    ['name' => 'Pixel 7', 'category' => 'Phone', 'price' => 599, 'weight' => 197],
    ['name' => 'LG Monitor', 'category' => 'Monitor', 'price' => 199, 'size' => 24]
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $filteredProducts = [];
    $category = $_POST['category'] ?? '';
    
    foreach ($products as $product) {
        if ($product['category'] !== $category) continue;
        
        $match = true;
        
        if (isset($_POST['price_min']) && $_POST['price_min'] !== '' && $product['price'] < (float)$_POST['price_min']) {
            $match = false;
        }
        if (isset($_POST['price_max']) && $_POST['price_max'] !== '' && $product['price'] > (float)$_POST['price_max']) {
            $match = false;
        }
        
        if ($category === 'Phone' && isset($_POST['weight_min']) && $_POST['weight_min'] !== '' && $product['weight'] < (float)$_POST['weight_min']) {
            $match = false;
        }
        if ($category === 'Phone' && isset($_POST['weight_max']) && $_POST['weight_max'] !== '' && $product['weight'] > (float)$_POST['weight_max']) {
            $match = false;
        }
        
        if ($category === 'Monitor' && isset($_POST['size_min']) && $_POST['size_min'] !== '' && $product['size'] < (float)$_POST['size_min']) {
            $match = false;
        }
        if ($category === 'Monitor' && isset($_POST['size_max']) && $_POST['size_max'] !== '' && $product['size'] > (float)$_POST['size_max']) {
            $match = false;
        }
        
        if ($match) {
            $filteredProducts[] = $product;
        }
    }
    
    header('Content-Type: application/json');
    echo json_encode($filteredProducts);
    exit;
}

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

    $html = '<form id="filter-form" data-category="'.htmlspecialchars($selectedCategory).'">';
    foreach ($filters as $filterName => $range) {
        if ($range) {
            $html .= '<div class="filter">';
            $html .= '<label>'.ucfirst($filterName).'</label>';
            $html .= '<input type="number" placeholder="Min: '.$range['min'].'" name="'.$filterName.'_min" min="'.$range['min'].'" max="'.$range['max'].'">';
            $html .= '<input type="number" placeholder="Max: '.$range['max'].'" name="'.$filterName.'_max" min="'.$range['min'].'" max="'.$range['max'].'">';
            $html .= '</div>';
        }
    }
    $html .= '<button type="submit" id="submit-btn" disabled>Submit</button>';
    $html .= '</form>';
    echo $html;
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
        .filter input { margin-left: 5px; width: 100px; }
        #submit-btn { padding: 5px 15px; margin-top: 10px; }
        #submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }
        #results { margin-top: 20px; }
        .product { padding: 5px; border-bottom: 1px solid #ddd; }
    </style>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('.category').click(function() {
                const category = $(this).data('category');
                $('.filter-container').html('Loading...');
                $('#results').empty();
                
                $.get('index.php', {category: category}, function(data) {
                    $('.filter-container').html(data);
                });
            });
            
            $(document).on('input', '#filter-form input', function() {
                $('#submit-btn').prop('disabled', false);
            });

            $(document).on('submit', '#filter-form', function(e) {
                e.preventDefault();
                const formData = $(this).serializeArray();
                const category = $(this).data('category');

                formData.push({name: 'category', value: category});
                
                $.ajax({
                    type: 'POST',
                    url: 'index.php',
                    data: $.param(formData),
                    success: function(data) {
                        displayResults(data);
                    }
                });
            });
            
            function displayResults(products) {
                const $results = $('#results');
                $results.empty();
                
                if (products.length === 0) {
                    $results.html('<div>No products found</div>');
                    return;
                }
                
                products.forEach(function(product) {
                    const $product = $('<div class="product"></div>');
                    $product.append(`<strong>${product.name}</strong>`);

                    for (const key in product) {
                        if (key !== 'name') {
                            $product.append(`<div>${key}: ${product[key]}</div>`);
                        }
                    }
                    
                    $results.append($product);
                });
            }
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
    
    <div id="results">
    </div>
</body>
</html>