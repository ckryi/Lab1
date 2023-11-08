def get_unique_elements(lst):

    unique_elements = []

    for num in lst:
        if lst.count(num) <= 1:
            unique_elements.append(num)

    return unique_elements

input_list = [1, 2, 3, 1, 2, 4]
unique_list = get_unique_elements(input_list)
print(unique_list)