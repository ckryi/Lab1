try:
    password = input()
    confirmation = input()

    if password == confirmation:
        print("Password accepted")
    else:
        print("Password not accepted")

except ValueError:
    print("Bad Input")