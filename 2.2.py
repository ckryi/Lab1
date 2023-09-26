try:
    num = int(input())

    thousand = num // 1000
    hundred = (num // 100) % 10
    ten = (num // 10) % 10
    one = num % 10

    print(f"The digit in the thousands position is {thousand}")
    print(f"The number in the hundreds position is {hundred}")
    print(f"The digit in the tens position is {ten}")
    print(f"The digit in the position of units is {one}")
except ValueError:
    print("Bad input")