try:
    num = int(input())
    num = abs(num)
    
    digit_sum = 0
    
    while num > 0:
        digit = num % 10  #last num
        digit_sum += digit  #num + last num
        num //= 10  #remove last digit
        
    print(digit_sum)

except ValueError:
    print("Bad input")