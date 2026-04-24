let i = 0;
while (i <= 10){
    let num = Math.floor(Math.random() * 20) + 1;
    if (num % 4 != 0){
        console.log(num)
    }
    i ++;
}