try:
    age = int(input())

    if age < 0:
        raise ValueError("Bad Input")

    if age <= 13:
        print("Childhood")
    elif age <= 24:
        print("Youth")
    elif age <= 59:
        print("Maturity")
    else:
        print("Old age")

except ValueError:
    print("Bad Input")