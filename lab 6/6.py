def get_unique_elements_with_count(list):

    unique_elements = {}

    for element in list:
        if element in unique_elements:
            unique_elements[element] += 1
        else:
            unique_elements[element] = 1

    return unique_elements

input_list = [1, 2, 3, 1, 2, 4, 1]
result = get_unique_elements_with_count(input_list)
print(result)