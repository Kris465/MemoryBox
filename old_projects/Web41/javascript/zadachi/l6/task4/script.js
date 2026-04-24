class MyButton {
    constructor(text, btnClass) {
        this.text = text;
        this.btnClass = btnClass;
    }
    show() {
        document.write(<button type = "button" class = "btn ${this.btnClass}" >${this.text}</button>);

    }
    get value() {
        return this.text;
    }

    set value(newText) {
        this.text = newText;
    }
}

class ColorButton extends MyButton {
    constructor(text, btnClass, colorClass){
        super(text, btnClass);
        this.colorClass = colorClass;
    }
}