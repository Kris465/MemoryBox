const prompt = require('prompt-sync')();

function isRookThreatening(a, b, c, d) {
    return a === c || b === d; 
}

function isBishopThreatening(a, b, c, d) {
    return Math.abs(a - c) === Math.abs(b - d); 
}

function canKingMove(a, b, c, d) {
    return Math.abs(a - c) <= 1 && Math.abs(b - d) <= 1; 
}

function isQueenThreatening(a, b, c, d) {
    return isRookThreatening(a, b, c, d) || isBishopThreatening(a, b, c, d); 
}

function canWhitePawnMove(a, b, c, d) {
    const normalMove = (a === c && b + 1 === d); 
    const attackMove = (a === c - 1 && b + 1 === d);
    return normalMove || attackMove;
}

function canBlackPawnMove(a, b, c, d) {
    const normalMove = (a === c && b - 1 === d); 
    const attackMove = (a === c + 1 && b - 1 === d); 
    return normalMove || attackMove;
}

function isKnightThreatening(a, b, c, d) {
    const dx = Math.abs(a - c);
    const dy = Math.abs(b - d);
    return (dx === 2 && dy === 1) || (dx === 1 && dy === 2);
}

const a = parseInt(prompt("Введите номер вертикали для фигуры:"), 10);
const b = parseInt(prompt("Введите номер горизонтали для фигуры:"), 10);
const c = parseInt(prompt("Введите номер вертикали для клетки:"), 10);
const d = parseInt(prompt("Введите номер горизонтали для клетки:"), 10);

console.log(`Ладья угрожает: ${isRookThreatening(a,b,c,d)}`);
console.log(`Слон угрожает: ${isBishopThreatening(a,b,c,d)}`);
console.log(`Король может переместиться: ${canKingMove(a,b,c,d)}`);
console.log(`Ферзь угрожает: ${isQueenThreatening(a,b,c,d)}`);
console.log(`Белая пешка может переместиться: ${canWhitePawnMove(a,b,c,d)}`);
console.log(`Черная пешка может переместиться: ${canBlackPawnMove(a,b,c,d)}`);
console.log(`Конь угрожает: ${isKnightThreatening(a,b,c,d)}`);