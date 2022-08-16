let card1 = document.getElementById('first-card')
let card2 = document.getElementById('second-card')
let card3 = document.getElementById('third-card')
let blackjackButton = document.getElementById('blackjack')
let resultsDiv = document.getElementById('results')



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

blackjackButton.addEventListener('click', function() {
    console.log(card1, card2, card3) // a q 7
    let first_card = deck[card1.value.toUpperCase()]
    let second_card = deck[card2.value.toUpperCase()]
    let third_card = deck[card3.value.toUpperCase()]
    console.log(first_card, second_card, third_card) // 1 10 7
    total = add(first_card, second_card, third_card)
    console.log(total) // 18

    if (total < 17) {
        var answer = "Hit"
    } else if (total >= 17 && total < 21) {
        var answer = "Stay"
    } else if (total === 21) {
        var answer = "Blackjack!"
    } else if (total > 21) {
        var answer = "Busted!"
    }
    console.log(answer) // Stay

    let resultP = document.createElement('p')
    resultP.innerText = answer
    resultsDiv.prepend(resultP)

})

