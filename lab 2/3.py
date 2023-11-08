try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    diff = num2 - num1

    if num3 == num2 + diff:
        print("YES")
    else:
        print("NO")

except ValueError:
    print("Bad Input")