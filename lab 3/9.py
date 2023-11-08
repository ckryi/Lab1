import random

secret_number = random.randint(1, 100)

while True:
    try:
        user_guess = int(input())
        
        if user_guess < 1 or user_guess > 100:
            print("Bad Input")
            continue
        
        if user_guess < secret_number:
            print("Too small.")
        elif user_guess > secret_number:
            print("Too large.")
        else:
            print(f"Congratulations! It's: {secret_number}")
            break
    
    except ValueError:
        print("Bad Input")
