try:
    school_children = int(input())

    tangerines = int(input())

    get = tangerines // school_children

    remainings = tangerines % school_children

    print(get, remainings)
except ValueError:
    print("Bad input")