try:
    num = int(input())

    if num > 18:
        print("Access allowed")
    elif num == 18:
        print("Access allowed")
    else:
        print("Access denied")
except ValueError:
    print("Bad Input")        