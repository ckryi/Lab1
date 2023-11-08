try:
    char_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
    
    char_string = ''.join(char_tuple)
    
    print(f"The string is: '{char_string}'")

except ValueError:
    print("Bad Input")
