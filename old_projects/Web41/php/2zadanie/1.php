<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список изображений</title>
    <style>
        img {
            max-width: 200px; 
            margin: 10px; 
        }
    </style>
</head>
<body>

<h1>Список изображений</h1>

<?php

$directory = '.'; 


$images = glob($directory . '/*.{ jpg , jpeg , png , gif }', GLOB_BRACE);


if (!empty($images)) {
    foreach ($images as $image) {
        echo '<img src="' . htmlspecialchars($image) . '" alt="Image">';
    }
} else {
    echo '<p>Изображения не найдены.</p>';
}
?>

</body>
</html>
