function isPointInShadedArea(x, y) {
    const x1 = 1, y1 = 1; 
    const x2 = 5, y2 = 4;

    const inRectangle = (x >= x1 && x <= x2 && y >= y1 && y <= y2);

    const cx = 3, cy = 3, r = 2;

    const inCircle = (Math.pow(x - cx, 2) + Math.pow(y - cy, 2) <= Math.pow(r, 2));

    return inRectangle || inCircle;
}

const x = 2, y = 2;
if (isPointInShadedArea(x, y)) {
    console.log(`Точка (${x}, ${y}) попадает в заштрихованную область.`);
} else {
    console.log(`Точка (${x}, ${y}) не попадает в заштрихованную область.`);
}