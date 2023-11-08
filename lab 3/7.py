try:
    user_input = input()
    reversed_string = ""
    
    for char in reversed(user_input):
        reversed_string += char
    
    print(reversed_string)

except ValueError:
    print("Bad input.")