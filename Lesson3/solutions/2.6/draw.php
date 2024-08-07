<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $shape = $_POST['shape'];
    $x = intval($_POST['x']);
    $y = intval($_POST['y']);
    $color = $_POST['color'];

    $output = '';

    if ($shape == 'circle') {
        $output .= "<div class='circle' style='left: {$x}px; top: {$y}px; background-color: {$color};'></div>";
    } elseif ($shape == 'square') {
        $output .= "<div class='square' style='left: {$x}px; top: {$y}px; background-color: {$color};'></div>";
    } elseif ($shape == 'triangle') {
        $output .= "<div class='triangle' style='left: {$x}px; top: {$y}px; border-left: 25px solid transparent; border-right: 25px solid transparent; border-bottom: 50px solid {$color}; position: absolute; top: {$y}px; left: {$x}px;'></div>";
    }

    echo $output;
}
?>