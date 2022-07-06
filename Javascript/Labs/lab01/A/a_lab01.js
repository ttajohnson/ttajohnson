// Lab 01 Py-JS Conversion - Average Numbers -~-~-~-~

let nums = []

let invalidInput = true

while (invalidInput) {
    let num = prompt("Enter a number or done: ")
    if (num === "done") {
        invalidInput = false
    } else {
        nums.push(parseFloat(num))
    }
}
    

let sum = 0;
for (let n of nums)
    sum += n;

alert("The sum of your numbers is " + sum)

let quantity = nums.length

alert("There are " + quantity + " items in your list.")

let average = sum / quantity

alert("The average of your numbers is " + average)