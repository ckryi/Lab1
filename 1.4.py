try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    result = num1 + num2 + num3

    print(result)
except ValueError:
    print("Bad input")