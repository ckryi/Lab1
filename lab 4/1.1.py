try:
    user_input = input()
    
    char_tuple = tuple(user_input)
    
    print("Created tuple is:")
    print(char_tuple)

except ValueError:
    print("Bad Input")
