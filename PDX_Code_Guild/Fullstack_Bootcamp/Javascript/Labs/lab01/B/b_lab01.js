let nums = document.getElementById('nums')
let calcButton = document.getElementById('calculate')
let resultsDiv = document.getElementById('results')

calcButton.addEventListener('click', function() {
    console.log(nums.value) // 1, 2, 3, 4, 5
    let numList = nums.value
    let arrList = numList.split(', ')
    console.log(arrList) // [ "1", "2", "3", "4", "5" ]
    let arrNums = []
    arrList.forEach(str => {
        arrNums.push(Number(str))
    });
    console.log(arrNums) // [ 1, 2, 3, 4, 5 ]
    let sum = 0
    for (let num of arrNums)
        sum += num
    console.log(sum) // 15
    let quantity = arrNums.length
    console.log(quantity) // 5
    let average = sum / quantity
    console.log(average) // 3
    let resultP = document.createElement('p')
    resultP.innerText = "You have " + quantity + " numbers with the sum of " + sum + ". The average of these numbers is " + average + "."
    resultsDiv.prepend(resultP)
})