try:
    first_col = int(input())
    first_row = int(input())
    second_col = int(input())
    second_row = int(input())

    if abs(first_col - second_col) <= 1 and abs(first_row - second_row) <= 1:
        print("YES")
    else:
        print("NO")
        
except ValueError:
    print("Bad Input")