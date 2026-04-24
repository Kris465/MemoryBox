function findBoundingRectangle(rect1, rect2) {
    const [x1_1, y1_1, x1_2, y1_2] = rect1;
    const [x2_1, y2_1, x2_2, y2_2] = rect2;
    const x_min = Math.min(x1_1, x2_1);
    const y_min = Math.min(y1_1, y2_1);
    const x_max = Math.max(x1_2, x2_2);
    const y_max = Math.max(y1_2, y2_2);
    return {
        bottomLeft: { x: x_min, y: y_min },
        topRight: { x: x_max, y: y_max }
    };
}

const rectangle1 = [1, 1, 4, 4]; 
const rectangle2 = [2, 2, 5, 5];

const boundingRectangle = findBoundingRectangle(rectangle1, rectangle2);
console.log("Левый нижний угол:", boundingRectangle.bottomLeft);
console.log("Правый верхний угол:", boundingRectangle.topRight);