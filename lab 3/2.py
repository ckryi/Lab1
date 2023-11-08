try:
    N = int(input())
    
    if N < 0:
        raise ValueError()
    
    factorial = 1
    i = 1
    
    while i <= N:
        factorial *= i
        i += 1
        
    print(factorial)

except ValueError:
    print("Bad Input")
