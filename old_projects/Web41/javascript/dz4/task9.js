const prompt = require('prompt-sync')();
function convertSecondsToTimeFormat(totalSeconds)
    {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds / 60

    const formattedTime = `${String(hours).padStart(2, '0')} : ${String(minutes).padStart(2, '0')}: ${String(seconds).padStart (2, '0')}`;

   
    return formattedTime;


    }
const secondsInput = prompt('введите кол-во секунд:');
const totalSeconds = parseInt(secondsInput, 10);

const formattedTime = convertSecondsToTimeFormat(totalSeconds);

console.log(`вермя в формате "чч:мм:сс": ${formattedTime}`);