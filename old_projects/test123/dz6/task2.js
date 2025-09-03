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

    gcd(a, b) {
        return b === 0 ? a : this.gcd(b, a % b);
    }

    simplify() {
        const gcd = this.gcd(Math.abs(this.numerator), Math.abs(this.denominator));
        this.numerator /= gcd;
        this.denominator /= gcd;
        if (this.denominator < 0) { 
            this.numerator = -this.numerator;
            this.denominator = -this.denominator;
        }
    }

    add(fraction) {
        const newNumerator = this.numerator * fraction.denominator + fraction.numerator * this.denominator;
        const newDenominator = this.denominator * fraction.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    subtract(fraction) {
        const newNumerator = this.numerator * fraction.denominator - fraction.numerator * this.denominator;
        const newDenominator = this.denominator * fraction.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    multiply(fraction) {
        const newNumerator = this.numerator * fraction.numerator;
        const newDenominator = this.denominator * fraction.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    divide(fraction) {
        if (fraction.numerator === 0) {
            throw new Error("Деление на ноль невозможно.");
        }
        const newNumerator = this.numerator * fraction.denominator;
        const newDenominator = this.denominator * fraction.numerator;
        return new Fraction(newNumerator, newDenominator);
    }

    toString() {
        return `${this.numerator}/${this.denominator}`;
    }
}

const fraction1 = new Fraction(prompt('Введите числитель первой дроби: '), prompt('Введите знаменатель первой дроби: ')); 
const fraction2 = new Fraction(prompt('Введите числитель второй дроби: '), prompt('Введите знаменатель второй дроби: ')); 

const sum = fraction1.add(fraction2);
console.log(`Сумма: ${sum.toString()}`); 

const difference = fraction1.subtract(fraction2);
console.log(`Разность: ${difference.toString()}`); 

const product = fraction1.multiply(fraction2);
console.log(`Произведение: ${product.toString()}`); 

const quotient = fraction1.divide(fraction2);
console.log(`Частное: ${quotient.toString()}`); 

