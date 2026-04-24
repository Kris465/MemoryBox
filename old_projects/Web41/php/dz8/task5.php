<?php
function drawChessBoard($piece, $row, $col) {
    if ($row < 1 || $row > 8 || $col < 1 || $col > 8) {
        return "Неверные координаты. Строка и столбец должны быть от 1 до 8.";
    }

    $board = '<table style="border-collapse: collapse; width: 320px; height: 320px;">';

    for ($r = 8; $r >= 1; $r--) {
        $board .= '<tr>';
        for ($c = 1; $c <= 8; $c++) {
            $color = ($r + $c) % 2 == 0 ? '#ffffff' : '#cccccc'; 
            $board .= '<td style="width: 40px; height: 40px; background-color: ' . $color . '; text-align: center; vertical-align: middle; font-size: 24px;">';
            if ($r == $row && $c == $col) {
                $board .= htmlspecialchars($piece); 
            }

            $board .= '</td>';
        }
        $board .= '</tr>';
    }

    $board .= '</table>';
    return $board;
}

$piece = '';
$row = 0;
$col = 0;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $piece = $_POST['piece'];
    $row = (int)$_POST['row'];
    $col = (int)$_POST['col'];
}


$chessBoardHtml = drawChessBoard($piece, $row, $col);
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Шахматная доска</title>
</head>
<body>

<h1>Шахматная доска</h1>

<form method="post">
    <label for="piece">Введите фигуру (например, ♞, ♟, ♜):</label><br>
    <input type="text" id="piece" name="piece" required><br><br>
    
    <label for="row">Введите номер строки (1-8):</label><br>
    <input type="number" id="row" name="row" min="1" max="8" required><br><br>
    
    <label for="col">Введите номер столбца (1-8):</label><br>
    <input type="number" id="col" name="col" min="1" max="8" required><br><br>
    
    <input type="submit" value="Показать фигуру">
</form>

<div style="margin-top: 20px;">
    <?php echo $chessBoardHtml; ?>
</div>

</body>
</html>