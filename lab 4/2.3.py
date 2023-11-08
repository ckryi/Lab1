try:
    set_A = {1, 2, 3, 4, 5}
    set_B = {5, 7, 8, 9, 2, 10}

    set_A.difference_update(set_B)

    print(set_B)

except ValueError:
    print("Bad Input")
