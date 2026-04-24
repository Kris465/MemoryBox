const rookThreatens = (a, b, c, d) => (a === c || b === d);
const bishopThreatens = (a, b, c, d) => Math.abs(a - c) === Math.abs(b - d);
const kingCanMove = (a, b, c, d) => Math.abs(a - c) <= 1 && Math.abs(b - d) <= 1;
const queenThreatens = (a, b, c, d) => (a === c || b === d || Math.abs(a - c) === Math.abs(b - d));
const whitePawnMove = (a, b, c, d) => (a === c && b + 1 === d);
const whitePawnAttack = (a, b, c, d) => (a + 1 === c && b + 1 === d) || (a - 1 === c && b + 1 === d);
const blackPawnMove = (a, b, c, d) => (a === c && b - 1 === d);
const blackPawnAttack = (a, b, c, d) => (a + 1 === c && b - 1 === d) || (a - 1 === c && b - 1 === d);
const knightThreatens = (a, b, c, d) => 
    (Math.abs(a - c) === 2 && Math.abs(b - d) === 1) || 
    (Math.abs(a - c) === 1 && Math.abs(b - d) === 2);

const a = 4, b = 4; 
const c = 5, d = 5; 
    
console.log("Ладья угрожает:", rookThreatens(a, b, c, d));
console.log("Слон угрожает:", bishopThreatens(a, b, c, d));
console.log("Король может переместиться:", kingCanMove(a, b, c, d));
console.log("Ферзь угрожает:", queenThreatens(a, b, c, d));
console.log("Белая пешка может переместиться:", whitePawnMove(a, b, c, d));
console.log("Белая пешка может бить:", whitePawnAttack(a, b, c, d));
console.log("Черная пешка может переместиться:", blackPawnMove(a, b, c, d));
console.log("Черная пешка может бить:", blackPawnAttack(a, b, c, d));
console.log("Конь угрожает:", knightThreatens(a, b, c, d));