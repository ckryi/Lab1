try:
    set_A = {1, 2, 3, 4, 5}
    set_B = {5, 7, 8, 9, 2, 10}

    difference_set = set_A.symmetric_difference(set_B)

    print(difference_set)

except ValueError:
    print("Bad Input")
