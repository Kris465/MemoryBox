const prompt = require('prompt-sync')();

class Fraction {
    constructor(numerator, denominator) {
        if (denominator === 0) {
            throw new Error("Знаменатель не может быть равен нулю.");
        }
        this.numerator = numerator;
        this.denominator = denominator;
        this.simplify();
    }
    calculateGCD(a, b) {
        return b === 0 ? a : this.calculateGCD(b, a % b);
    }

    simplify() {
        const gcd = this.calculateGCD(Math.abs(this.numerator), Math.abs(this.denominator));
        this.numerator /= gcd;
        this.denominator /= gcd;
        if (this.denominator < 0) {
            this.numerator *= -1;
            this.denominator *= -1;
        }
    }

    add(other) {
        const newNumerator = this.numerator * other.denominator + other.numerator * this.denominator;
        const newDenominator = this.denominator * other.denominator;
        return new Fraction(newNumerator, newDenominator);

    }


    subtract(other) {
        const newNumerator = this.numerator * other.denominator - other.numerator * this.denominator;
        const newDenominator = this.denominator * other.denominator;
        return new Fraction(newNumerator, newDenominator);
    }


    multiply(other) {
        const newNumerator = this.numerator * other.numerator;
        const newDenominator = this.denominator * other.denominator;
        return new Fraction(newNumerator, newDenominator);
    }


     divide(other) {
        if (other.numerator === 0) {
            throw new Error("Деление на ноль невозможно.");
        }
        const newNumerator = this.numerator * other.denominator;
        const newDenominator = this.denominator * other.numerator;
        return new Fraction(newNumerator, newDenominator);
    }

    
    toString() {
        return `${this.numerator}/${this.denominator}`;

 }
 
}

const fraction1 = new Fraction(3, 4);
const fraction2 = new Fraction(2, 5);

console.log("Дробь 1:", fraction1.toString()); 
console.log("Дробь 2:", fraction2.toString()); 

const sum = fraction1.add(fraction2);
console.log("Сумма:", sum.toString()); 

const difference = fraction1.subtract(fraction2);
console.log("Разность:", difference.toString());

const product = fraction1.multiply(fraction2);
console.log("Произведение:", product.toString()); 

const quotient = fraction1.divide(fraction2);
console.log("Частное:", quotient.toString());

