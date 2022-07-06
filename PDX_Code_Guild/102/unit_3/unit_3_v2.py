meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}

distance = input('What is the distance? ')
distance = int(distance)
units = input('What are the units? (ft, mi, m, km, yd, in) ')

m = meters[units]

output = distance * m

print(f'{distance} {units} is {output} m')