try:
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))

    operation = input("Please choose the operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("division by zero isn't allowed!!!")
    else:
        print("choose an operation!")
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Bad input")