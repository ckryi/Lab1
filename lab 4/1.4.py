try:
    input_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)

    element_count = {}
    for item in input_tuple:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

    result_tuple = [(item, count) for item, count in element_count.items()]

    print("Elements and their occurrences:")
    print(tuple(result_tuple))

except ValueError:
    print("Bad Input")
