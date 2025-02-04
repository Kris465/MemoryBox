const prompt = require('prompt-sync')(); 

const styles = [
    { name: 'color', value: 'blue' },
    { name: 'font-size', value: '20px' },
    { name: 'text-align', value: 'center' },
    { name: 'text-decoration', value: 'underline' }
];

function applyStyles(stylesArray, text) {
    const styleString = stylesArray.map(style => `${style.name}: ${style.value};`).join(' ');
    const output = `<p style="${styleString}">${text}</p>`;
    document.write(output);
}

applyStyles(styles, 'Привет, мир!');
