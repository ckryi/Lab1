try:
    set_A = {1, 2, 3, 4, 7}
    set_B = {8, 7, 9, 4, 2, 0, 10}
    set_C = {4, 0, 1}

    for element in set_C.copy():
        if element in set_A:
            set_A.remove(element)
            set_B.add(element)
        set_C.update(set_A)

    print(set_A)
    print(set_B)
    print(set_C)

except ValueError:
    print("Bad Input")
