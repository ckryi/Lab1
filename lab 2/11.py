try:
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        print(num2)
    else:
        print(num1)

except ValueError:
    print("Bad Input")