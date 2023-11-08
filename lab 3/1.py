try:
    N = int(input())
    
    if N <= 0:
        raise ValueError()
    
    i = 2  
    while i <= N:
        print(i)
        i += 2  

except ValueError:
    print("Bad Input")