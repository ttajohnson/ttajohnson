# VERSION 1 - ft to m
# def v1_unit_converter():
#     m = 0.3048
#     distance = int(input('What is the distance in feet? '))
#     result = distance * m
#     print(f'{distance} ft is {result} m')

# v1_unit_converter()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# VERSION 2 - choice to m

# def v2_unit_converter():
#     distance = int(input('What is the distance? \n'))
#     units = input("What are the units? (ft, mi, m, km) \n").lower()
#     if units == "ft":
#         m = 0.3048
#     elif units == "mi":
#         m = 1609.34
#     elif units == "m":
#         m = 1
#     elif units == "km":
#         m = 1000
#     result = distance * m
#     print(f'{distance} {units} is {result} m')

# v2_unit_converter()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# VERSION 3 - add yards & inches

# def v3_unit_converter():
#     distance = int(input('What is the distance? \n'))
#     units = input("What are the units? (ft, mi, m, km, yd, in) \n").lower()
#     if units == "ft":
#         m = 0.3048
#     elif units == "mi":
#         m = 1609.34
#     elif units == "m":
#         m = 1
#     elif units == "km":
#         m = 1000
#     elif units == "yd":
#         m = 0.9144
#     elif units == "in":
#         m = 0.0254
#     result = distance * m
#     print(f'{distance} {units} is {result} m')

# v3_unit_converter()

# ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# VERSION 4 - FULL VERSION

units_in_meters = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm'  : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

def to_meters(distance, units):
    return distance * units_in_meters[units]

def from_meters(distance, units):
    return distance / units_in_meters[units]

def standardize_units(units):
    if units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['mi', 'mile', 'miles']:
        return 'mi'
    elif units in ['ft', 'feet']:
        return 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'
    elif units in ['yd', 'yard', 'yards']:
        return 'yd'
    elif units in ['in', 'inch', 'inches']:
        return 'in'

def main():

    print("- Welcome to Tim's Unit Converter -")

    while True:
        try:
            distance = float(input('Enter your distance: '))
            break
        except ValueError as e:
            print(e)
            print('Error: Please enter a number')
            pass

    while True:
        units = standardize_units(input('Enter your starting units: '))
        if units:
            break

    while True:
        target_units = standardize_units(input('Enter your desired units: '))
        if target_units:
            break

    distance_to_meters = to_meters(distance, units)

    meters_to_units = from_meters(distance_to_meters, target_units)

    print(f'{distance} {units} is {round(meters_to_units, 4)} {target_units}')

main()


