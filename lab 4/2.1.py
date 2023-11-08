try:
    user_input = input()
    
    char_set = {char for char in user_input}
    
    print(char_set)

except ValueError:
    print("Bad Input")