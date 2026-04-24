
const isUnderThreat = (c, d, e, f) => {
    const rookThreatens = (c, d, e, f) => (c === e || d === f);
    const queenThreatens = (c, d, e, f) => (c === e || d === f || Math.abs(c - e) === Math.abs(d - f));
    const knightThreatens = (c, d, e, f) => 
        (Math.abs(c - e) === 2 && Math.abs(d - f) === 1) || 
        (Math.abs(c - e) === 1 && Math.abs(d - f) === 2);
    const bishopThreatens = (c, d, e, f) => Math.abs(c - e) === Math.abs(d - f);
    
    return rookThreatens(c, d, e, f) || queenThreatens(c, d, e, f) || knightThreatens(c, d, e, f) || bishopThreatens(c, d, e, f);
};
const canMoveWithoutThreat = (a, b, e, f, c, d, whitePiece) => {
    let canMove = false;

    switch (whitePiece) {
        case 'rook':
            canMove = (a === e || b === f);
            break;
        case 'queen':
            canMove = (a === e || b === f || Math.abs(a - e) === Math.abs(b - f));
            break;
        case 'knight':
            canMove = (Math.abs(a - e) === 2 && Math.abs(b - f) === 1) || 
                       (Math.abs(a - e) === 1 && Math.abs(b - f) === 2);
            break;
        case 'bishop':
            canMove = Math.abs(a - e) === Math.abs(b - f);
            break;
        case 'king':
            canMove = Math.abs(a - e) <= 1 && Math.abs(b - f) <= 1;
            break;
    }
    return canMove && !isUnderThreat(c, d, e, f);
};

const a = 4, b = 4; 
const c = 5, d = 5; 
const e = 4, f = 5;

console.log("Ладья и Ладья:", canMoveWithoutThreat(a, b, e, f, c, d, 'rook'));
console.log("Ферзь и Ферзь:", canMoveWithoutThreat(a, b, e, f, c, d, 'queen'));
console.log("Конь и Конь:", canMoveWithoutThreat(a, b, e, f, c, d, 'knight'));
console.log("Слон и Слон:", canMoveWithoutThreat(a, b, e, f, c, d, 'bishop'));
console.log("Король и Слон:", canMoveWithoutThreat(a, b, e, f, c, d, 'king'));
