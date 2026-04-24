const prompt = require('prompt-sync')();

const teams = [
  { wins: 10, losses: 5 },
  { wins: 8, losses: 9 },
  { wins: 12, losses: 4 },
  { wins: 7, losses: 7 },
  { wins: 15, losses: 3 }
]; 

let countMoreWins = 0;

for (let team of teams) {
    if (team.wins > team.losses) {
        countMoreWins++;
    }
}

console.log(`Количество команд с большим количеством побед, чем поражений: ${countMoreWins}`);