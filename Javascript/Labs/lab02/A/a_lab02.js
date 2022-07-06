// Py to JS

let deck = {
    "A": 1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10
}

function add(a, b, c) {
    return a + b + c
}

let card1 = deck[prompt("What is your first card?").toUpperCase()]
let card2 = deck[prompt("What is your second card?").toUpperCase()]
let card3 = deck[prompt("What is your third card?").toUpperCase()]

alert(card1 + card2 + card3)


if  (add(card1, card2, card3) < 17) {
    alert('Hit')
}   else if (add(card1, card2, card3) >= 17 && add(card1, card2, card3) < 21) {
    alert('Stay')
}   else if (add(card1, card2, card3) === 21) {
    alert('Blackjack!')
}   else if (add(card1, card2, card3) > 21) {
    alert('Busted!')
}

