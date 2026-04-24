
function evaluateExpressions(X, Y) {
    const notXAndNotY = !X && !Y; 
    const XOrNotXAndY = X || (!X && Y); 
    const NotXAndYOrY = (!X && Y) || Y; 

    console.log(`X: ${X}, Y: ${Y}`);
    console.log(`а) не X и не Y: ${notXAndNotY}`);
    console.log(`б) X или (не X и Y): ${XOrNotXAndY}`);
    console.log(`в) (не X и Y) или Y: ${NotXAndYOrY}`);
    console.log('-------------------');
}


function getBooleanInput(promptMessage) {
    let input;
    do {
        input = prompt(promptMessage + " (введите 'true' или 'false'):");
    } while (input !== 'true' && input !== 'false');
    return input === 'true';
}


const X = getBooleanInput("Введите значение для X");
const Y = getBooleanInput("Введите значение для Y");


evaluateExpressions(X, Y);