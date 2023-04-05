let nums = []


while (true) {
    let newNum = prompt("Enter a number!")

    if (newNum === "Done") {
        break
    } else if (!isNaN(parseFloat(newNum))) {
        nums.push(parseFloat(newNum))
    }
}

let sum = nums.reduce((nums, val) => nums + val, 0)
let nums_length = nums.length

let total = sum/nums_length


console.log(nums_length)
alert(`Your numbers were ${nums}, the sum of those numbers is ${sum}. The average of those numbers is ${total}`)