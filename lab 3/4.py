try:
    user_input = input()
    user_input = user_input.lower()
    
    a = user_input.count("a")
    
    print(a)
except ValueError:
    print("Bad input")