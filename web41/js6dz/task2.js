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
        const gcdValue = this.gcd(Math.abs(this.numerator), Math.abs(this.denominator));
        this.numerator /= gcdValue;
        this.denominator /= gcdValue;

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
            throw new Error("Деление на ноль.");
        }
        const newNumerator = this.numerator * fraction.denominator;
        const newDenominator = this.denominator * fraction.numerator;
        return new Fraction(newNumerator, newDenominator);
    }
    toString() {
        return `${this.numerator}/${this.denominator}`;
    }
}
const fraction1 = new Fraction(1, 2);
const fraction2 = new Fraction(3, 4);

console.log(`Сложение: ${fraction1.add(fraction2).toString()}`);
console.log(`Вычитание: ${fraction1.subtract(fraction2).toString()}`);
console.log(`Умножение: ${fraction1.multiply(fraction2).toString()}`);
console.log(`Деление: ${fraction1.divide(fraction2).toString()}`);
