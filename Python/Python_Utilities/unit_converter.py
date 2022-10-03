def unit_converter():

    input_units = input("What are the input units: ")
    distance = int(input("What is the distance: "))

    if input_units == "ft":
        m_input = 0.3048
    elif input_units == "mi":
        m_input = 1609.34
    elif input_units == "m":
        m_input = 1
    elif input_units == "km":
        m_input = 1000
    elif input_units == "in":
        m_input = 0.0254
    elif input_units == "yd":
        m_input = 0.9144

    input_result = distance * m_input

    output_units = input("What are the output units: ")

    if output_units == "ft":
        m_output = 0.3048
    elif output_units == "mi":
        m_output = 1609.34
    elif output_units == "m":
        m_output = 1
    elif output_units == "km":
        m_output = 1000
    elif output_units == "in":
        m_output = 0.0254
    elif output_units == "yd":
        m_output = 0.9144

    final_result = input_result / m_output

    print(f'{distance} {input_units} is {final_result} {output_units}.')

unit_converter()