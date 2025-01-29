class MyButton {
    constructor(text, btnClass) {
        this.text = text;
        this.btnClass = btnClass;
    }

    show() {
        document.write(<button type="button" class="btn ${this.btnClass}">${this.text}</button>);
    }

    get value() {
        return this.text;
    }

    set value(newText) {
        this.text = newText;
    }
}

class ColorButton extends MyButton {
    constructor(text, btnClass, colorClass) {
        super(text, btnClass);
        this.colorClass = colorClass;
    }

    show() {
        document.write(<button type="button" class="btn ${this.colorClass}">${this.text}</button>);
    }
}

let saveButton = new MyButton("Save Progress", "btn-success");
let clickMeButton = new MyButton("Click Me", "btn-secondary");
let downloadButton = new MyButton("Download", "btn-secondary");
let seeMoreButton = new ColorButton("See more", "btn", "btn-danger");

saveButton.show();
clickMeButton.show();
downloadButton.show();
seeMoreButton.show();

clickMeButton.value = "Updated Click Me";
clickMeButton.show();
