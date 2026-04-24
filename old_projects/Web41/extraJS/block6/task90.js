const prompt = require('prompt-sync')(); 
let a = prompt('введите а: ');
let b = prompt('введите b: ');
         
while (a >= b) {    
  console.log(Math.sqrt(a));
  a--;              
}
          
do {
  console.log(Math.sqrt(a));
  a--;              
} while (a >= b);   
