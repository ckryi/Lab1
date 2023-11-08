try:
    input = input()
    list = [char.lower() for char in input]
    count = [(char, list.count(char)) for char in set(list)]
    print(count)
except ValueError:
    print("Bad input")