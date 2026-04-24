let sentence = "Это предложение содержит s1 и ещё одно s1.";
let s1 = "s1"; 
let s2 = "s2"; 

let result = sentence.replace(new RegExp(s1, 'g'), s2);
console.log(result);