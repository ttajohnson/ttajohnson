// let a = document.getElementById('Your-equation: ');
// let bs = document.getElementsByTagName('div');
// console.log(bs.length); // 3                     
// let cs = document.getElementsByName('adiv');                                        
// console.log(cs.length); // 2                    
// let d = document.querySelector('#mydiv');
// let es = document.querySelectorAll('.myclass');

// let btn = document.getElementById('btn') // Best to put all your element gets at the top

// // let num1 = parseFloat(prompt('first number?'))
// // let num2 = parseFloat(prompt('second number?'))

// let num1 = 2
// let num2 = 2

// // a.innerHTML += `<strong><em>${num1} + ${num2} = ${num1 + num2}</em></strong>`
// a.innerText = `${num1} + ${num2} = ${num1 + num2}`
// a.id = 'mynewdiv' // Changes the ID afterrr running the above innerText change

// // You technically can use javascript to make all your CSS, but best to only use this for one-off styling.
// //Large case should stay in .css file.
// a.style.backgroundColor = 'red' // CSS properties, converted to camelCase
// a.style.color = 'white'
// a.style.padding = '2em'
// // a.className = 'newclass' // lets your specify a class for an element, or change the existing class


// for (let i=0; i<bs.length;i++) {
//     console.log(bs[i])
//     if (i %2 === 0) {
//         bs[i].style.backgroundColor = 'green'
//     } else {
//         bs[i].style.backgroundColor = 'blue'
//     }  
// }


// let brandNewElement = document.createElement('p')
// brandNewElement.innerText = "I'm a brand new p!"
// brandNewElement.style.backgroundColor = 'purple'
// brandNewElement.style.color = 'whitesmoke'
// brandNewElement.style.padding = '2rem'
// brandNewElement.classList.add('super-cool-class')
// brandNewElement.id = 'brand-new-element'

// a.appendChild(brandNewElement)

// // ---EVENTS---

// function runMe(event) {
//     alert("Hello World!")
//     alert(`You clicked on [${event.x}, ${event.y}]`)
//     console.log(event)
// }

// btn.addEventListener('click', runMe) // NO paranthessis on runMe function makes it happen on click/every time.

// // // btn.addEventListener('click', function() { //the anonymous version of this function does the same, but does need the paranthesis
// // //     alert("Hello World!")
// // // })

// let num1 = document.getElementById('num1')
// let num2 = document.getElementById('num2')
// let resultsDiv = document.getElementById('results')
// let calculateBtn = document.getElementById('calculate')

// // console.log(num1)
// // console.log(num2)
// // console.log(resultsP)
// // console.log(calculateBtn)

// calculateBtn.addEventListener('click', function() {
//     let answer = parseFloat(num1.value) + parseFloat(num2.value)
//     let resultP = document.createElement('p')
//     resultP.innerText = answer
//     // resultsDiv.prependChild(resultP) // newer, compatibility issues
//     resultsDiv.insertBefore(resultP, resultsDiv.firstChild) // more complicated, but compatible
// })

let nums = document.getElementsByClassName('num')
let resultsDiv = document.getElementById('results')
let calculateBtn = document.getElementById('calculate')
let numDiv = document.getElementById('num-div')
let addNumBtn = document.getElementById('add-num')

addNumBtn.addEventListener('click', function() {
    let newNum = document.createElement('input')
    newNum.type = 'number'
    newNum.classList.add('num')

    let newNumRemove = document.createElement('button')
    newNumRemove.innerText = '×'
    newNumRemove.addEventListener('click', function() {
        newNum.remove()
        newNumRemove.remove()
    })


    numDiv.appendChild(newNum)
    numDiv.appendChild(newNumRemove)
})

calculateBtn.addEventListener('click', function() {
    let answer =0
    for (let i=0; i<nums.length; i++) {
        if (nums[i].value === "") {
            nums[i].value = 0
        }
        answer += parseFloat(nums[i].value)
    }
    let resultP = document.createElement('p')
    resultP.innerText = answer
    resultsDiv.prepend(resultP) // newer, compatibility issues
//     resultsDiv.insertBefore(resultP, resultsDiv.firstChild) // more complicated, but compatible
})