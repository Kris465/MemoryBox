const characters = [
    { name: "Персонаж 1", rarity: "common" },
    { name: "Персонаж 2", rarity: "rare" },
    { name: "Персонаж 3", rarity: "epic" },
    { name: "Персонаж 4", rarity: "legendary" },
];

const drawButton = document.getElementById("drawButton");
const resultDiv = document.getElementById("result");

drawButton.addEventListener("click", () => {
    const drawnCharacter = drawCharacter();
    resultDiv.textContent = `Выброшен: ${drawnCharacter.name} (${drawnCharacter.rarity})`;
});

function drawCharacter() {
    const rarityWeights = {
        common: 70,
        rare: 20,
        epic: 9,
        legendary: 1,
    };

    const totalWeight = Object.values(rarityWeights).reduce((a, b) => a + b, 0);
    const randomNum = Math.random() * totalWeight;

    let cumulativeWeight = 0;

    for (const character of characters) {
        cumulativeWeight += rarityWeights[character.rarity];
        if (randomNum < cumulativeWeight) {
            return character;
        }
    }
}
