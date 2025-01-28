class Rounds {
    constructor(id, color) {
        this.id = id;
        this.color = color;
    }
    changeColor() {
        let greys = document.getElementsByClassName('grey-round');
        
        document.getElementById('r1').classList.add('grey-round');
        document.getElementById('r2').classList.add('grey-round');
        document.getElementById('r3').classList.add('grey-round');
        document.getElementById(this.id).classList.remove('grey-round');
    }
    getHtml() {
        document.write(`<div class="round grey-round" id="${this.id}" style="background-color: ${this.color}"></div>`)
    }
}

let i = 0;
let index = 1;

function toggle() {
    if (i == 0) {
        index = 1;
        r1.changeColor();
    }
    else if (i == 1) {
        r2.changeColor();
    }
    else if (i == 2) {
        r3.changeColor();
    }
    if (i < 2) {
        i += index;
    }
    else {
        index = -1;
        i += index;
    };
}

r1 = new Rounds('r1', 'red');
r2 = new Rounds('r2', 'yellow');
r3 = new Rounds('r3', 'green');

r1.getHtml();
r2.getHtml();
r3.getHtml();