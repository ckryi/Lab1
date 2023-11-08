try:
    input = input()
    list = [char.lower() for char in input]
    print(list)
except ValueError:
    print("Bad input")