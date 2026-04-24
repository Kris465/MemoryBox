function findBoundingRectangle(rect1, rect2) {
    const { x: x1, y: y1, width: width1, height: height1 } = rect1;
    const { x: x2, y: y2, width: width2, height: height2 } = rect2;

    const x1_max = x1 + width1;
    const y1_max = y1 + height1;

    const x2_max = x2 + width2;
    const y2_max = y2 + height2;

    const x_min = Math.min(x1, x2);
    const y_min = Math.min(y1, y2);

    const x_max = Math.max(x1_max, x2_max);
    const y_max = Math.max(y1_max, y2_max);

    return {
        bottomLeft: { x: x_min, y: y_min },
        topRight: { x: x_max, y: y_max }
    };
}
const rectangle1 = { x: 1, y: 1, width: 3, height: 2 }; 
const rectangle2 = { x: 2, y: 2, width: 4, height: 3 }; 

const boundingRectangle = findBoundingRectangle(rectangle1, rectangle2);
console.log("Левый нижний угол:", boundingRectangle.bottomLeft);
console.log("Правый верхний угол:", boundingRectangle.topRight);