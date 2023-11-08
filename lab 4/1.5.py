try:
    input_data = (55, 6, 777, 70.0, '7', 'A')

    integer_tuple = tuple(item for item in input_data if isinstance(item, int))
    float_tuple = tuple(item for item in input_data if isinstance(item, float))
    string_tuple = tuple(item for item in input_data if isinstance(item, str))

    print(integer_tuple)
    print(float_tuple)
    print(string_tuple)

except ValueError:
    print("Bad Input")
