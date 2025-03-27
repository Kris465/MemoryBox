<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Дурак - исправленная версия</title>
    <style>
        body {
            background: grey;
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .card {
            width: 60px;
            height: 90px;
            background: white;
            border: 1px solid #333;
            border-radius: 5px;
            margin: 5px;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            font-size: 20px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            transition: all 0.3s;
        }
        .card.trump {
            border: 2px solid red;
        }
        .card.defend-option {
            box-shadow: 0 0 10px blue;
        }
        .card.computer-card {
            background-color: #f0f0f0;
        }
        .player-area, .computer-area, .table-area {
            margin: 20px 0;
            padding: 15px;
            border: 1px dashed #ccc;
            min-height: 100px;
        }
        .table-area {
            background-color: #508550;
        }
        button {
            padding: 10px 15px;
            margin: 5px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:disabled {
            background-color: #cccccc;
        }
        .info-panel {
            padding: 10px;
            background-color: #8f8aa3;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .message {
            padding: 10px;
            margin: 10px 0;
            background-color: #fffde7;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="game-container">
        <h1>Дурак (исправленная версия)</h1>
        
        <div class="info-panel">
            <div>Козырь: <span id="trump-card"></span></div>
            <div>Карт в колоде: <span id="deck-count">36</span></div>
            <div>Ход: <span id="current-turn">Компьютера</span></div>
            <div class="message" id="message">Компьютер ходит...</div>
        </div>
        
        <div class="computer-area">
            <h3>Компьютер (<span id="computer-cards">6</span> карт)</h3>
            <div id="computer-cards-container"></div>
        </div>
        
        <div class="table-area" id="table">
            <h3>Стол</h3>
            <div id="attack-cards"></div>
            <div id="defend-cards"></div>
        </div>
        
        <div class="player-area">
            <h3>Вы (<span id="player-cards">6</span> карт)</h3>
            <div id="player-cards-container"></div>
        </div>
        
        <div class="controls">
            <button id="take-cards" disabled>Взять карты</button>
            <button id="end-turn" disabled>Бито</button>
        </div>
    </div>

    <script>
        class DurakGame {
            constructor() {
                this.suits = ['hearts', 'diamonds', 'clubs', 'spades'];
                this.ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
                this.deck = [];
                this.trump = null;
                this.trumpCard = null;
                this.playerCards = [];
                this.computerCards = [];
                this.attackCards = [];
                this.defendCards = [];
                this.currentTurn = 'computer';
                this.gameOver = false;
                this.lastAttacker = 'computer';
                this.computerDefendCard = null;
                
                this.initGame();
            }
            
            initGame() {
                this.createDeck();
                this.shuffleDeck();
                this.setTrump();
                this.dealCards();
            }
            
            createDeck() {
                this.deck = [];
                for (let suit of this.suits) {
                    for (let rank of this.ranks) {
                        this.deck.push({ suit, rank });
                    }
                }
            }
            
            shuffleDeck() {
                for (let i = this.deck.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [this.deck[i], this.deck[j]] = [this.deck[j], this.deck[i]];
                }
            }
            
            setTrump() {
                if (this.deck.length > 0) {
                    this.trumpCard = this.deck[0];
                    this.trump = this.trumpCard.suit;
                }
            }
            
            dealCards() {
                const initialCards = 6;
                while (this.playerCards.length < initialCards && this.deck.length > 0) {
                    this.playerCards.push(this.deck.pop());
                }
                while (this.computerCards.length < initialCards && this.deck.length > 0) {
                    this.computerCards.push(this.deck.pop());
                }
            }
            
            playerAttack(cardIndex) {
                if (this.currentTurn !== 'player' || this.lastAttacker === 'player') return false;
                
                const card = this.playerCards[cardIndex];
                
                if (this.attackCards.length > 0) {
                    const existingRanks = this.getAllTableCards().map(c => c.rank);
                    if (!existingRanks.includes(card.rank)) {
                        return false;
                    }
                }
                
                this.attackCards.push(card);
                this.playerCards.splice(cardIndex, 1);
                this.lastAttacker = 'player';
                this.currentTurn = 'computer';
                return true;
            }
            
            playerDefend(cardIndex) {
                if (this.currentTurn !== 'player' || this.attackCards.length === 0) return false;
                
                const attackCard = this.attackCards[this.defendCards.length];
                const defendCard = this.playerCards[cardIndex];
                
                if (!this.canDefend(attackCard, defendCard)) {
                    return false;
                }
                
                this.defendCards.push({
                    attack: attackCard,
                    defend: defendCard
                });
                this.playerCards.splice(cardIndex, 1);
                
                if (this.defendCards.length === this.attackCards.length) {
                    this.completeDefense();
                }
                
                return true;
            }
            
            canDefend(attackCard, defendCard) {
                if (defendCard.suit === this.trump) {
                    if (attackCard.suit === this.trump) {
                        return this.getCardValue(defendCard) > this.getCardValue(attackCard);
                    }
                    return true;
                }
                
                return (defendCard.suit === attackCard.suit) && 
                       (this.getCardValue(defendCard) > this.getCardValue(attackCard);
            }
            
            completeDefense() {
                this.attackCards = [];
                this.defendCards = [];
                this.computerDefendCard = null;
                this.currentTurn = this.lastAttacker === 'player' ? 'computer' : 'player';
                this.refillCards();
            }
            
            getCardValue(card) {
                return this.ranks.indexOf(card.rank);
            }
            
            getAllTableCards() {
                return [
                    ...this.attackCards,
                    ...this.defendCards.map(pair => pair.attack),
                    ...this.defendCards.map(pair => pair.defend)
                ].filter(Boolean);
            }
            
            refillCards() {
                while (this.playerCards.length < 6 && this.deck.length > 0) {
                    this.playerCards.push(this.deck.pop());
                }
                while (this.computerCards.length < 6 && this.deck.length > 0) {
                    this.computerCards.push(this.deck.pop());
                }
            }
            
            playerTakeCards() {
                this.playerCards.push(...this.attackCards);
                this.attackCards = [];
                this.defendCards = [];
                this.computerDefendCard = null;
                this.currentTurn = 'computer';
                this.lastAttacker = 'computer';
                this.refillCards();
            }
            
            endTurn() {
                this.attackCards = [];
                this.defendCards = [];
                this.computerDefendCard = null;
                this.currentTurn = this.lastAttacker === 'player' ? 'computer' : 'player';
                this.refillCards();
            }
            
            checkGameOver() {
                if (this.playerCards.length === 0 && this.deck.length === 0) {
                    this.gameOver = true;
                    return 'player';
                }
                if (this.computerCards.length === 0 && this.deck.length === 0) {
                    this.gameOver = true;
                    return 'computer';
                }
                return null;
            }
            
            computerDefend() {
                const attackCard = this.attackCards[this.defendCards.length];
                const possibleDefends = this.computerCards
                    .map((card, index) => ({card, index}))
                    .filter(({card}) => this.canDefend(attackCard, card));
                
                if (possibleDefends.length === 0) {
                    this.computerCards.push(...this.attackCards);
                    this.attackCards = [];
                    this.defendCards = [];
                    this.computerDefendCard = null;
                    this.currentTurn = 'player';
                    this.lastAttacker = 'player';
                    this.refillCards();
                    return false;
                }
                
                possibleDefends.sort((a, b) => this.getCardValue(a.card) - this.getCardValue(b.card));
                const {card, index} = possibleDefends[0];
                
                this.computerDefendCard = card;
                this.defendCards.push({
                    attack: attackCard,
                    defend: card
                });
                this.computerCards.splice(index, 1);
                
                if (this.defendCards.length === this.attackCards.length) {
                    this.completeDefense();
                }
                
                return true;
            }
            
            computerAttack() {
                if (this.computerCards.length === 0) return false;
                
                // Сортируем карты по значению (от меньшего к большему)
                this.computerCards.sort((a, b) => this.getCardValue(a) - this.getCardValue(b));
                
                // Если на столе уже есть карты, ищем карту такого же достоинства
                if (this.attackCards.length > 0) {
                    const existingRanks = this.getAllTableCards().map(c => c.rank);
                    for (let card of this.computerCards) {
                        if (existingRanks.includes(card.rank)) {
                            const cardIndex = this.computerCards.indexOf(card);
                            this.attackCards.push(card);
                            this.computerCards.splice(cardIndex, 1);
                            this.lastAttacker = 'computer';
                            this.currentTurn = 'player';
                            return true;
                        }
                    }
                    return false;
                }
                
                // Если стол пустой - атакуем самой слабой картой
                const attackCard = this.computerCards[0];
                this.attackCards.push(attackCard);
                this.computerCards.splice(0, 1);
                this.lastAttacker = 'computer';
                this.currentTurn = 'player';
                return true;
            }
        }

        class DurakUI {
            constructor(game) {
                this.game = game;
                this.initUI();
                this.updateUI();
                this.setupEventListeners();
            }
            
            initUI() {
                this.playerCardsContainer = document.getElementById('player-cards-container');
                this.computerCardsContainer = document.getElementById('computer-cards-container');
                this.attackCardsContainer = document.getElementById('attack-cards');
                this.defendCardsContainer = document.getElementById('defend-cards');
                this.trumpCardElement = document.getElementById('trump-card');
                this.deckCountElement = document.getElementById('deck-count');
                this.playerCardsCount = document.getElementById('player-cards');
                this.computerCardsCount = document.getElementById('computer-cards');
                this.currentTurnElement = document.getElementById('current-turn');
                this.takeCardsButton = document.getElementById('take-cards');
                this.endTurnButton = document.getElementById('end-turn');
                this.messageElement = document.getElementById('message');
            }
            
            updateUI() {
                this.playerCardsContainer.innerHTML = '';
                this.game.playerCards.forEach((card, index) => {
                    const cardElement = this.createCardElement(card, index, true);
                    
                    if (this.game.currentTurn === 'player' && 
                        this.game.attackCards.length > 0 && 
                        this.game.defendCards.length < this.game.attackCards.length) {
                        
                        const attackCard = this.game.attackCards[this.game.defendCards.length];
                        if (this.game.canDefend(attackCard, card)) {
                            cardElement.classList.add('defend-option');
                        }
                    }
                    
                    this.playerCardsContainer.appendChild(cardElement);
                });
                
                this.computerCardsContainer.innerHTML = '';
                this.game.computerCards.forEach((card, index) => {
                    const cardElement = document.createElement('div');
                    cardElement.className = 'card computer-card';
                    cardElement.textContent = '🂠';
                    this.computerCardsContainer.appendChild(cardElement);
                });
                
                this.attackCardsContainer.innerHTML = '';
                this.game.attackCards.forEach((card, index) => {
                    if (index >= this.game.defendCards.length) {
                        const cardElement = this.createCardElement(card, -1, false);
                        this.attackCardsContainer.appendChild(cardElement);
                    }
                });
                
                this.defendCardsContainer.innerHTML = '';
                this.game.defendCards.forEach(pair => {
                    const attackCard = this.createCardElement(pair.attack, -1, false);
                    const defendCard = this.createCardElement(pair.defend, -1, false);
                    
                    const pairContainer = document.createElement('div');
                    pairContainer.style.display = 'inline-block';
                    pairContainer.style.margin = '5px';
                    pairContainer.appendChild(attackCard);
                    pairContainer.appendChild(defendCard);
                    
                    this.defendCardsContainer.appendChild(pairContainer);
                });
                
                if (this.game.computerDefendCard) {
                    const defendCardElement = this.createCardElement(this.game.computerDefendCard, -1, false);
                    defendCardElement.classList.add('computer-card');
                    this.defendCardsContainer.appendChild(defendCardElement);
                }
                
                this.trumpCardElement.textContent = this.getCardSymbol(this.game.trumpCard);
                this.trumpCardElement.className = 'card';
                if (this.game.trumpCard.suit === this.game.trump) {
                    this.trumpCardElement.classList.add('trump');
                }
                
                this.deckCountElement.textContent = this.game.deck.length;
                this.playerCardsCount.textContent = this.game.playerCards.length;
                this.computerCardsCount.textContent = this.game.computerCards.length;
                
                this.currentTurnElement.textContent = this.game.currentTurn === 'player' ? 'Ваш' : 'Компьютера';
                
                this.takeCardsButton.disabled = 
                    this.game.currentTurn !== 'player' || 
                    this.game.attackCards.length === 0;
                
                this.endTurnButton.disabled = 
                    this.game.currentTurn !== 'player' || 
                    this.game.attackCards.length === 0 ||
                    this.game.defendCards.length < this.game.attackCards.length;
                
                if (this.game.currentTurn === 'player') {
                    if (this.game.attackCards.length > 0 && 
                        this.game.defendCards.length < this.game.attackCards.length) {
                        this.messageElement.textContent = 'Выберите карту для отбития';
                    } else if (this.game.lastAttacker !== 'player') {
                        this.messageElement.textContent = 'Выберите карту для атаки';
                    } else {
                        this.messageElement.textContent = 'Ожидайте хода компьютера';
                    }
                } else {
                    this.messageElement.textContent = 'Ход компьютера...';
                }
            }
            
            createCardElement(card, index, clickable) {
                const cardElement = document.createElement('div');
                cardElement.className = 'card';
                if (card.suit === this.game.trump) {
                    cardElement.classList.add('trump');
                }
                cardElement.textContent = this.getCardSymbol(card);
                
                if (clickable) {
                    cardElement.addEventListener('click', () => this.handleCardClick(index));
                }
                
                return cardElement;
            }
            
            getCardSymbol(card) {
                const rankSymbols = {
                    'J': 'В', 'Q': 'Д',
                    'K': 'К', 'A': 'Т'
                };
                
                const rank = rankSymbols[card.rank] || card.rank;
                const suitSymbol = this.getSuitSymbol(card.suit);
                
                return `${rank}${suitSymbol}`;
            }
            
            getSuitSymbol(suit) {
                const symbols = {
                    'hearts': '♥', 'diamonds': '♦',
                    'clubs': '♣', 'spades': '♠'
                };
                return symbols[suit] || suit;
            }
            
            setupEventListeners() {
                this.takeCardsButton.addEventListener('click', () => {
                    this.game.playerTakeCards();
                    this.updateUI();
                    
                    const winner = this.game.checkGameOver();
                    if (winner) {
                        this.showGameOver(winner);
                        return;
                    }
                    
                    setTimeout(() => {
                        this.computerTurn();
                    }, 1000);
                });
                
                this.endTurnButton.addEventListener('click', () => {
                    this.game.endTurn();
                    this.updateUI();
                    
                    const winner = this.game.checkGameOver();
                    if (winner) {
                        this.showGameOver(winner);
                        return;
                    }
                    
                    setTimeout(() => {
                        this.computerTurn();
                    }, 1000);
                });
            }
            
            handleCardClick(index) {
                if (this.game.currentTurn === 'player') {
                    if (this.game.attackCards.length > 0 && 
                        this.game.defendCards.length < this.game.attackCards.length) {
                        const success = this.game.playerDefend(index);
                        if (success) {
                            this.updateUI();
                            
                            const winner = this.game.checkGameOver();
                            if (winner) {
                                this.showGameOver(winner);
                                return;
                            }
                            
                            if (this.game.defendCards.length < this.game.attackCards.length) {
                                this.messageElement.textContent = 'Продолжайте отбиваться';
                            } else {
                                setTimeout(() => {
                                    this.computerTurn();
                                }, 1000);
                            }
                        }
                    } else if (this.game.lastAttacker !== 'player') {
                        const success = this.game.playerAttack(index);
                        if (success) {
                            this.updateUI();
                            
                            const winner = this.game.checkGameOver();
                            if (winner) {
                                this.showGameOver(winner);
                                return;
                            }
                            
                            setTimeout(() => {
                                this.computerTurn();
                            }, 1000);
                        }
                    }
                }
            }
            
            computerTurn() {
                if (this.game.gameOver) return;
                if (this.game.currentTurn !== 'computer') {
                    this.updateUI();
                    return;
                }

                setTimeout(() => {
                    // 1. Сначала пытаемся отбиться
                    if (this.game.attackCards.length > 0 && 
                        this.game.defendCards.length < this.game.attackCards.length) {
                        
                        const defended = this.game.computerDefend();
                        this.updateUI();
                        
                        if (defended && this.game.defendCards.length < this.game.attackCards.length) {
                            // Если еще нужно отбиваться - продолжаем
                            this.computerTurn();
                        }
                        return;
                    }
                    
                    // 2. Если не нужно отбиваться - пытаемся атаковать
                    if (this.game.lastAttacker !== 'computer') {
                        const attacked = this.game.computerAttack();
                        this.updateUI();
                    }
                }, 1000);
            }
            
            showGameOver(winner) {
                alert(winner === 'player' ? 
                    'Поздравляем! Вы выиграли!' : 
                    'Компьютер выиграл. Попробуйте еще раз!');
                
                location.reload();
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            const game = new DurakGame();
            const ui = new DurakUI(game);
            
            setTimeout(() => {
                ui.computerTurn();
            }, 1000);
        });
    </script>
</body>
</html>