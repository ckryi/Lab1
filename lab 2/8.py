try:
    weight = int(input())
    if weight <= 0:
        raise ValueError("Bad Input")

    if weight <= 60:
        print("Light weight")
    elif weight <= 64:
        print("First welterweight")
    elif weight <= 69:
        print("Welterweight")
    else:
        print("Unknown weight category")

except ValueError:
    print("Bad Input")