try:
    first_col = int(input())
    first_row = int(input())
    second_col = int(input())
    second_row = int(input())

    if first_col == second_col or first_row == second_row:
        print("YES")
    else:
        print("NO")

except ValueError:
    print("Bad Input")