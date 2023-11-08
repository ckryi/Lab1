import itertools

try:
    A = {1, 2, 3, 4, 5, 6}
    n = 3
    m = 5

    combinations = list(itertools.combinations(A, n))
    
    if len(combinations) < m:
        print("Wrong Input.")
    else:
        result = [set(combo) for combo in combinations[:m]]
        print(result)

except ValueError:
    print("Bad Input")
