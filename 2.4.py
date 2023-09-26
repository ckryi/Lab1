try: 
    num = int(input())

    result = num << 1

    if result == 0:
        print("Warning: The result is zero.")
    else:
        print(f"The result of << is: {result}")
except ValueError:
    print("Bad input")