def get_elements_with_no_more_than_two_occurrences(list):

    count_dict = {}

    for num in list:
        count_dict[num] = count_dict.get(num, 0) + 1

    result = []

    for num, count in count_dict.items():
        if count <= 2:
            result.append(num)

    return result