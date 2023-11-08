try:
    num = int(input())

    thousand = num // 1000
    hundred = (num // 100) % 10
    ten = (num // 10) % 10
    one = num % 10

    if thousand + one == hundred - ten:
        print("yes")
    else:
        print("no")

except ValueError:
    print("Bad input")