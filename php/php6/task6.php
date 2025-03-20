<?php

$sections = [
    'Header' => [
        'height' => '100px',
        'background_color' => '#4CAF50',
        'text_color' => '#FFFFFF'
    ],
    'Content' => [
        'height' => '300px',
        'background_color' => '#F1F1F1',
        'text_color' => '#333333'
    ],
    'Footer' => [
        'height' => '80px',
        'background_color' => '#333333',
        'text_color' => '#FFFFFF'
    ]
];
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Страница с секциями</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .section {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <?php foreach ($sections as $name => $properties): ?>
        <div class="section" 
             style="height: <?php echo $properties['height']; ?>; 
                    background-color: <?php echo $properties['background_color']; ?>; 
                    color: <?php echo $properties['text_color']; ?>;">
            <?php echo $name; ?>
        </div>
    <?php endforeach; ?>
</body>
</html>