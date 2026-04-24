function determineRegion(x, y) {
    if (y > 0) {
        if (x > 0) {
            return "Область I"; 
        } else {
            return "Область II";
        }
    } else {
        return "Точка находится ниже оси X"; 
    }
}

const points = [
    { x: 1, y: 2 },   
    { x: -1, y: 2 }, 
    { x: 1, y: -2 },  
    { x: -1, y: -2 }, 
    { x: 0, y: 2 },  
];

points.forEach(point => {
    console.log(`Точка (${point.x}, ${point.y}) попадает в: ${determineRegion(point.x, point.y)}`);
});