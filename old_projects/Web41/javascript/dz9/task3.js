const prompt = require('prompt-sync')();

class CssClass {
    constructor(className) {
        this.className = className; 
        this.styles = []; 
    }

    setStyle(property, value) {
        const existingStyle = this.styles.find(style => style.property === property);
        if (existingStyle) {
            existingStyle.value = value; 
        } else {
            this.styles.push({ property, value }); 
        }
    }

    removeStyle(property) {
        this.styles = this.styles.filter(style => style.property !== property); 
    }

    getCss() {
        const stylesString = this.styles.map(style => `${style.property}: ${style.value};`).join(' ');
        return `.${this.className} { ${stylesString} }`;
    }
}

const buttonClass = new CssClass('button');
buttonClass.setStyle('background-color', 'blue');
buttonClass.setStyle('color', 'white');
buttonClass.setStyle('border', 'none');

console.log(buttonClass.getCss()); 

buttonClass.removeStyle('border');
console.log(buttonClass.getCss()); 