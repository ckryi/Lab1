while True:
    try:
        number = int(input())
        
        if number == 42:
            print("Bad Input.")
            break
    except ValueError:
        print("Bad Input")
