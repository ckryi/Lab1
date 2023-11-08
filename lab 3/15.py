try:
    user_input = input()
    shift = int(input())

    encrypted_text = ""

    for char in user_input:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    print(encrypted_text)

except ValueError:
    print("Bad input")
