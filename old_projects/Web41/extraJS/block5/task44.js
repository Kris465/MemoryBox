function totalWeight(weights) {

    const totalMass = weights.reduce((accumulator, current) => accumulator + current, 0);
    return totalMass;
}


const weights = [10.5, 20.3, 15.0, 5.2]; 

const result = totalWeight(weights);
console.log(`Общая масса груза: ${result} кг`);