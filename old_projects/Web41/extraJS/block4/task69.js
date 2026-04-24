function isRectangle1InsideRectangle2(x1, y1, width1, height1, x2, y2, width2, height2) {
    const rect1BottomLeft = { x: x1, y: y1 };
    const rect1TopRight = { x: x1 + width1, y: y1 + height1 };
    
    const rect2BottomLeft = { x: x2, y: y2 };
    const rect2TopRight = { x: x2 + width2, y: y2 + height2 };

    return (
        rect1BottomLeft.x >= rect2BottomLeft.x &&
        rect1BottomLeft.y >= rect2BottomLeft.y &&
        rect1TopRight.x <= rect2TopRight.x &&
        rect1TopRight.y <= rect2TopRight.y
    );
}

function isRectangleInsideAnother(x1, y1, width1, height1, x2, y2, width2, height2) {
    return isRectangle1InsideRectangle2(x1, y1, width1, height1, x2, y2, width2, height2) ||
           isRectangle1InsideRectangle2(x2, y2, width2, height2, x1, y1, width1, height1);
}

function doRectanglesIntersect(x1, y1, width1, height1, x2, y2, width2, height2) {
    const rectA = { left: x1, right: x1 + width1, bottom: y1 , top: y1 + height1 };
    const rectB = { left: x2 , right: x2 + width2 , bottom: y2 , top: y2 + height2 };

    if (rectA.right <= rectB.left || rectB.right <= rectA.left) {
        return false;
    }

    if (rectA.top <= rectB.bottom || rectB.top <= rectA.bottom) {
        return false;
    }

    return true; 
}

const xP1 = 0;
const yP1 = 0;
const widthP1 = 4;
const heightP1 = 4;

const xP2 = 3;
const yP2 = 3;
const widthP2 = 4;
const heightP2 = 4;

console.log(isRectangleInsideAnother(xP1,yP1,widthP1,heightP1,xP2,yP2,widthP2,heightP2)); 
console.log(doRectanglesIntersect(xP1,yP1,widthP1,heightP11,xP22,yP22,widthP22,heightP22)); 