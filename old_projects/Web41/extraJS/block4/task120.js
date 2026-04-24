const prompt = require('prompt-sync')();

function isRookThreatening(c, d, e, f) {
    return c === e || d === f;
}

function isBishopThreatening(c, d, e, f) {
    return Math.abs(c - e) === Math.abs(d - f);
}

function canKingMove(a, b, e, f) {
    return Math.abs(a - e) <= 1 && Math.abs(b - f) <= 1; 
}

function isQueenThreatening(c, d, e, f) {
    return isRookThreatening(c, d, e, f) || isBishopThreatening(c, d, e, f); 
}

function canKnightMove(a, b, e, f) {
    const dx = Math.abs(a - e);
    const dy = Math.abs(b - f);
    return (dx === 2 && dy === 1) || (dx === 1 && dy === 2); 
}

function canWhitePieceMoveWithoutThreat(a, b, c, d, e, f) {
    const whiteCanMove = {
        'rook': isRookThreatening(a,b,e,f),
        'bishop': isBishopThreatening(a,b,e,f),
        'queen': isQueenThreatening(a,b,e,f),
        'knight': canKnightMove(a,b,e,f),
        'king': canKingMove(a,b,e,f)
    };

    const blackThreatens = {
        'rook': isRookThreatening(c,d,e,f),
        'bishop': isBishopThreatening(c,d,e,f),
        'queen': isQueenThreatening(c,d,e,f),
        'knight': canKnightMove(c,d,e,f),
        'king': canKingMove(c,d,e,f)
    };

    for (let whitePiece in whiteCanMove) {
        for (let blackPiece in blackThreatens) {
            if (whiteCanMove[whitePiece] && !blackThreatens[blackPiece]) {
                console.log(`Белая ${whitePiece} может пойти на (${e}, ${f}) без угрозы от черной ${blackPiece}`);
            }
        }
    }
}

// Пример использования:
const a = parseInt(prompt("Введите номер вертикали для белой фигуры:"), 10);
const b = parseInt(prompt("Введите номер горизонтали для белой фигуры:"), 10);
const c = parseInt(prompt("Введите номер вертикали для черной фигуры:"), 10);
const d = parseInt(prompt("Введите номер горизонтали для черной фигуры:"), 10);
const e = parseInt(prompt("Введите номер вертикали для целевой клетки:"), 10);
const f = parseInt(prompt("Введите номер горизонтали для целевой клетки:"), 10);

canWhitePieceMoveWithoutThreat(a,b,c,d,e,f);