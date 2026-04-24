const prompt = require('prompt-sync')();

function willHitTarget(v0, angle, R, H) {
    const g = 9.8;
    
    const angleRad = angle * (Math.PI / 180);
    
    const timeToReachR = R / (v0 * Math.cos(angleRad));
    
    const yAtR = (v0 * Math.sin(angleRad) * timeToReachR) - (0.5 * g * Math.pow(timeToReachR, 2));
    
    if (yAtR >= H) {
        return `Снаряд поразит цель на высоте ${H} м на расстоянии ${R} м.`;
    } else {
        return `Снаряд не поразит цель на высоте ${H} м на расстоянии ${R} м.`;
    }
}


const v0 = 50; 
const angle = 45; 
const R = 100; 
const H = 20; 

const result = willHitTarget(v0, angle, R, H);
console.log(result);