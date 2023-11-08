def get_keys_with_value_true(dict):
   
    if not isinstance(dict, dict):
        raise TypeError("Input should be a dictionary.")

    keys_with_value_true = []

    for key, value in dict.items():
        if value == True:
            keys_with_value_true.append(key)

    return keys_with_value_true

input_dict = {
    "a": True,
    "b": False,
    "c": True
}

output_list = get_keys_with_value_true(input_dict)
print(output_list)