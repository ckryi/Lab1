try:
    X = float(input())
    Y = int(input())
    
    result = 1
    count = 0
    
    while count < abs(Y):
        if Y > 0:
            result *= X
        else:
            result /= X
        count += 1
    
    print(result)

except (ValueError, ZeroDivisionError):
    print("Bad input")