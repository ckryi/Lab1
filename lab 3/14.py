def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    user_input = int(input())
    
    if user_input <= 1:
        print("Not prime.")
        user_input = 2
    
    while True:
        if is_prime(user_input):
            print(user_input)
            break
        else:
            user_input += 1
            continue

except ValueError:
    print("Bad input")
