try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 == num2 or num1 == num3 or num2 == num3:
        raise ValueError("Bad Input")
    else:
        sorted_nums = sorted([num1, num2, num3])
        print((sorted_nums[1]))

except ValueError:
    print("Bad Input")