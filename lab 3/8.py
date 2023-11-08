try:
    n = int(input())
    
    if n <= 0:
        raise ValueError()
    
    odd = 0
    
    for _ in range(n):
        num = int(input())
        
        if num % 2 == 0:
            continue
        
        odd += num
    print(odd)


except ValueError:
    print("Bad input")