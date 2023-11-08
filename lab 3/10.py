try:
    user_input = input()
    
    new_input = user_input.replace(" ", "").lower()
    
    if new_input == new_input[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

except ValueError:
    print("Bad input.")