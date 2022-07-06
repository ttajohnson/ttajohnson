unit_converter = {'m': 0.3048}

feet = input('\nWhat is the distance in feet? ')

feet = int(feet)

distance = feet * unit_converter['m']

print(f'{feet} ft is {distance} m')