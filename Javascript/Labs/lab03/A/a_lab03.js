// Py to JS Lab03 Pick 6

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

// let numbers = pick6()

// alert(numbers)
    
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

// let winning = pick6()
// let ticket = pick6()

// let match = num_matches(winning, ticket)

// alert(match)


let wallet = 0
let winner = 0
let expenses = 0
let winning = pick6()

alert("The winning numbers are " + winning + ". Good luck!")

for (let p = 0; p < 100000; p++) {
    ticket = pick6()
    wallet -= 2
    expenses += 2
    winner += num_matches(winning, ticket)
}



let final_balance = wallet + winner

let roi = (winner - expenses)/expenses


alert("After playing 100,000 times your final balance is: $" + final_balance)
alert("Your earnings were $" + winner + ". Your expenses were $" + expenses + ". Your ROI is " + roi + "%")