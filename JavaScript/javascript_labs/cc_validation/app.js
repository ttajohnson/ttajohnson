let ccNumber = prompt("Please enter a valid Credit Card Number:");

while (isNaN(ccNumber) || ccNumber.length < 16) {
    ccNumber = prompt("Please enter a valid Credit Card Number:");
}

// console.log(ccNumber)

let ccNumberList = ccNumber.split("").map(function(num) {
    return parseInt(num, 10);
})

console.log(ccNumberList)

let lastNum = ccNumberList.pop();

console.log(ccNumberList)
console.log(lastNum)

ccNumberList.reverse();

console.log(ccNumberList)

for (let i = 0; i < ccNumberList.length; i++) {
    if (i % 2 == 0) {
        ccNumberList[i] *= 2;
    }
}

console.log(ccNumberList)

for (let i in ccNumberList) {
    let num = ccNumberList[i];
    if (num > 9) {
        ccNumberList[i] -= 9;
    }
}

console.log(ccNumberList)

let ccListSum = ccNumberList.reduce((acc, val) => acc + val, 0);

console.log(ccListSum)

let lastDigit = ccListSum % 10;

console.log(lastDigit)
console.log(lastNum)

if (lastDigit === lastNum) {
    alert("Thank you for entering a valid Credit Card Number!")
} else {
    alert("Invalid Credit Card Number!")
}