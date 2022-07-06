let winningTicket = document.getElementById('winningTicket')
let plays = document.getElementById('plays')
let playBtn = document.getElementById('playsButton')
let results = document.getElementById('results')

function pick6() {
    
    let nums = []
    
    let i=6
    
    function randint(a, b) {
        return Math.floor(a + Math.random()*(b-a+1))
    }
    
    while (i > nums.length) {
        let rand = randint(1, 99)
        nums.push(rand)
    }
    
    return nums
}

function num_matches(winning, ticket) {
    let money = {
        0:0,
        1:4,
        2:7,
        3:100,
        4:50000,
        5:1000000,
        6:25000000
    }

    let matches = 0

    for (let i = 0; i<ticket.length; i++) {
        if (winning[i] === ticket[i]) {
            matches += 1
        }
    }   earnings = money[matches]
    return earnings
}

let winning = pick6()
let displayTicket = document.createElement('h3')
displayTicket.innerText = "The winning numbers are " + winning + ". Good luck!"
winningTicket.append(displayTicket)

playBtn.addEventListener('click', function() {
    let wallet = 0
    let winner = 0
    let expenses = 0
    for (let p = 0; p < plays.value; p++) {
        ticket = pick6()
        wallet -= 2
        expenses += 2
        winner += num_matches(winning, ticket)
    }
    let final_balance = wallet + winner
    let roi = (winner - expenses)/expenses
    console.log(plays.value, wallet, winner, expenses, final_balance, roi)

    let resultP = document.createElement('p')
    resultP.innerText = `---
    You bought ${plays.value} tickets for $${expenses}.

    Your winnings totaled $${winner}.

    Your final balance is $${final_balance}.

    That's an ROI of ${roi}%.
    ---`
    results.prepend(resultP)
})

