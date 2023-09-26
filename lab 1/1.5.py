try:
    value = int(input())

    volume = value ** 3

    area = 6 * value ** 2

    print('Volume = ' + str(volume), '\nTotal surface area = ' + str(area))
except ValueError:
    print("Bad input")