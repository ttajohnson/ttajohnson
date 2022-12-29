# LAB 01: UNIT CONVERTER
# This lab will involve writing a program that allows the user to convert a
# number between units.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1
# Ask the user for the number of feet, and print out the equivalent distance in
# meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by
# multiplying the input distance by 0.3048.

# >>>
# distance = input("Distance in feet: ")  # Receive distance from user.

# meter_total = int(distance) * 0.3048  # Convert input string to int and multiply.

# print(f"{distance} feet is {meter_total} meters")  # Print output in f-string.
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2
# Allow the user to also enter the units. Then depending on the units, convert
# the distance into meters. The units we'll allow are feet, miles, meters, and
# kilometers.

# >>>
# conversions = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000}

# distance = input("Distance: ")
# units = input("Units: ")

# total = int(distance) * conversions.get(units)

# print(f"{distance} {units} is {total} meters.")
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 3
# Add support for yards, and inches.

# >>>
# conversions = {
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "m": 1,
#     "km": 1000,
#     "yd": 0.9144,
#     "in": 0.0254,
# }

# distance = input("Distance: ")
# units = input("Units: ")

# total = int(distance) * conversions.get(units)

# print(f"{distance} {units} is {total} meters.")
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 4
# Now we'll ask the user for the distance, the starting units, and the units to
# convert to.

# >>>
conversions = {
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "m": 1,
    "km": 1000,
    "mi": 1609.34,
}

distance = input("Distance: ")
in_units = input("Input Units: ")
out_units = input("Output Units: ")

total = int(distance) * conversions.get(in_units) / conversions.get(out_units)

print(f"{distance} {in_units} is {round(total, 3)} {out_units}")
# >>>
