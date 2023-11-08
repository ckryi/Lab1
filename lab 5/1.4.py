try:
    list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

    sorted_list = sorted(list_A)

    n = len(sorted_list)
    q1_end = n // 4
    q2_end = q1_end * 2
    q3_end = q1_end * 3

    q1 = sorted_list[:q1_end]
    q2 = sorted_list[q1_end:q2_end]
    q3 = sorted_list[q2_end:q3_end]
    q4 = sorted_list[q3_end:]

    if n % 4 == 1:
        q1.append(0)

    print("q1 =", q1)
    print("q2 =", q2)
    print("q3 =", q3)
    print("q4 =", q4)

except ValueError:
    print("Bad input")