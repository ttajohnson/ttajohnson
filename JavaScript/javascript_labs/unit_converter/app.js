let unitConversions = {
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "m": 1,
    "km": 1000,
    "mi": 1609.34
}

let distance = Number(prompt("Distance: "))

let inUnits = prompt("Input Units: ")

let outUnits = prompt("Output Units: ")

let total = distance * unitConversions[inUnits] / unitConversions[outUnits]
let truncTotal = Math.trunc(total * 100) / 100

console.log(total)
alert(`${distance} ${inUnits} = ${truncTotal} ${outUnits}`)