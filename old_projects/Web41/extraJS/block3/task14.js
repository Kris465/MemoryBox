const values = [true, false];

function evaluateExpressions(X, Y) {
    const notOr = !(X || Y); 
    const notXAndY = !X && Y; 
    const XAndNotY = X && !Y; 
    console.log(`X: ${X}, Y: ${Y}`);
    console.log(`а) не (X или Y): ${notOr}`);
    console.log(`б) не X и Y: ${notXAndY}`);
    console.log(`в) X и не Y: ${XAndNotY}`);
    console.log('-------------------');
}
for (let X of values) {
    for (let Y of values) {
        evaluateExpressions(X, Y);
    }
}