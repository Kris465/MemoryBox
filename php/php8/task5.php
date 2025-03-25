<?php
/**
 * @param int|null 
 * @param int|null
 * @param string|null 
 * @param string|null 
 * @return string 
 */
function drawChessBoard(?int $pieceRow = null, ?int $pieceCol = null, ?string $pieceName = null, ?string $pieceColor = null): string {
    $hasPiece = false;
    if ($pieceRow !== null && $pieceCol !== null && $pieceName !== null && $pieceColor !== null) {
        if ($pieceRow >= 1 && $pieceRow <= 8 && $pieceCol >= 1 && $pieceCol <= 8) {
            $hasPiece = true;
        }
    }
    $unicodePieces = [
        'white' => [
            'king' => '♔',
            'queen' => '♕',
            'rook' => '♖',
            'bishop' => '♗',
            'knight' => '♘',
            'pawn' => '♙'
        ],
        'black' => [
            'king' => '♚',
            'queen' => '♛',
            'rook' => '♜',
            'bishop' => '♝',
            'knight' => '♞',
            'pawn' => '♟'
        ]
    ];
    $boardHtml = '<div class="chess-board">';

    for ($row = 1; $row <= 8; $row++) {
        for ($col = 1; $col <= 8; $col++) {
            $cellColor = (($row + $col) % 2 === 0) ? 'white' : 'black';

            $pieceSymbol = '';
            if ($hasPiece && $row === $pieceRow && $col === $pieceCol) {
                $pieceSymbol = $unicodePieces[strtolower($pieceColor)][strtolower($pieceName)] ?? '';
            }
            
            $boardHtml .= sprintf(
                '<div class="chess-cell %s">%s</div>',
                $cellColor,
                $pieceSymbol
            );
        }
    }
    
    $boardHtml .= '</div>';
    return $boardHtml;
}

$pieceRow = isset($_POST['row']) ? (int)$_POST['row'] : null;
$pieceCol = isset($_POST['col']) ? (int)$_POST['col'] : null;
$pieceName = $_POST['piece'] ?? null;
$pieceColor = $_POST['color'] ?? null;
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Полная шахматная доска</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        .chess-board {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            grid-template-rows: repeat(8, 60px);
            width: 480px;
            height: 480px;
            border: 2px solid #333;
            margin-bottom: 20px;
        }
        .chess-cell {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
        }
        .chess-cell.white {
            background-color: #f0d9b5;
        }
        .chess-cell.black {
            background-color: #b58863;
        }
        .controls {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            width: 480px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background: #45a049;
        }
        .coordinates {
            display: flex;
            justify-content: space-between;
            width: 480px;
            margin-bottom: 5px;
        }
        .coordinates span {
            width: 60px;
            text-align: center;
            font-weight: bold;
        }
        .row-coordinates {
            display: flex;
            flex-direction: column;
            margin-right: 5px;
        }
        .row-coordinates span {
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }
        .board-container {
            display: flex;
        }
    </style>
</head>
<body>
    <h1>Шахматная доска с фигурами</h1>
    
    <div class="board-container">
        <div class="row-coordinates">
            <?php for ($i = 8; $i >= 1; $i--) echo '<span>' . $i . '</span>'; ?>
        </div>
        <div>
            <div class="coordinates">
                <?php for ($i = 0; $i < 8; $i++) echo '<span>' . chr(97 + $i) . '</span>'; ?>
            </div>
            <?php echo drawChessBoard($pieceRow, $pieceCol, $pieceName, $pieceColor); ?>
        </div>
    </div>
    
    <div class="controls">
        <form method="POST">
            <div class="form-group">
                <label for="row">Строка (1-8):</label>
                <input type="number" id="row" name="row" min="1" max="8" required>
            </div>
            <div class="form-group">
                <label for="col">Столбец (1-8):</label>
                <input type="number" id="col" name="col" min="1" max="8" required>
            </div>
            <div class="form-group">
                <label for="piece">Фигура:</label>
                <select id="piece" name="piece" required>
                    <option value="pawn">Пешка</option>
                    <option value="rook">Ладья</option>
                    <option value="knight">Конь</option>
                    <option value="bishop">Слон</option>
                    <option value="queen">Ферзь</option>
                    <option value="king">Король</option>
                </select>
            </div>
            <div class="form-group">
                <label for="color">Цвет:</label>
                <select id="color" name="color" required>
                    <option value="white">Белые</option>
                    <option value="black">Чёрные</option>
                </select>
            </div>
            <button type="submit">Показать фигуру на доске</button>
        </form>
    </div>
</body>
</html>