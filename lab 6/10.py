def get_decimal_number_from_binary_string(binary_string):

    if not all(char in '01' for char in binary_string):
        raise ValueError("Bad input")

    decimal_number = int(binary_string, 2)

    return decimal_number

binary_string = "10110011"
decimal_number = get_decimal_number_from_binary_string(binary_string)
print(decimal_number)