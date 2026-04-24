const prompt = require('prompt-sync')();

class Marker {
    constructor(color, inkAmount) {
        this.color = color;
        this.inkAmount = inkAmount; 
    }

    print(text) {
        if (this.inkAmount <= 0) {
            console.log("Маркер не имеет чернил!");
            return;
        }

        let inkConsumed = 0;
        const symbolsToPrint = text.split('').filter(char => char !== ' ').length;
        const maxSymbols = Math.floor(this.inkAmount / 0.5); 

        const symbolsToDisplay = Math.min(symbolsToPrint, maxSymbols);
        let printedText = '';

        for (let i = 0; i < symbolsToDisplay; i++) {
            printedText += text[i] !== ' ' ? text[i] : ' ';
            inkConsumed += 0.5; 
        }

       
        this.inkAmount -= inkConsumed;

      
        console.log(`%c${printedText}`, `color: ${this.color};`);
    }
}

class RefillableMarker extends Marker {
    constructor(color2, inkAmount2) {
        super(color, inkAmount);
    }

    refill(amount) {
        this.inkAmount = Math.min(100, this.inkAmount + amount); 
        console.log(`Маркер заправлен. Текущие чернила: ${this.inkAmount}%`);
    }
}

const color = prompt("введите цвет: ");
const inkAmount = prompt("введите кол-во чернил: ");
const marker = new Marker(color, inkAmount);
marker.print("Это обычный маркер"); 

const color2 = prompt("введите цвет: ");
const inkAmount2 = prompt("введите кол-во чернил: ");
const refillableMarker = new RefillableMarker(color2, inkAmount2);
refillableMarker.print("Это наполняемый маркер."); 

refillableMarker.refill(30);
refillableMarker.print("Теперь здесь больше чернил.");