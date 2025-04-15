<?php
$categories = [
    'Phone' => 'PhoneCategory',
    'Monitor' => 'MonitorCategory'
];

$products = [
    ['name' => 'iPhone', 'type' => 'Phone'],
    ['name' => 'Samsung Monitor', 'type' => 'Monitor'],
    ['name' => 'Pixel', 'type' => 'Phone']
];

$listProducts = [];

foreach ($products as $product) {
    if (isset($categories[$product['type']])) {
        $listProducts[] = [
            'name' => $product['name'],
            'category' => $categories[$product['type']]
        ];
    }
}

print_r($listProducts);
?>