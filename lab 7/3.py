def count_uppercase_characters(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        uppercase_count = sum(1 for char in content if char.isupper())
    return uppercase_count

file_path = 'file3.txt'
uppercase_count = count_uppercase_characters(file_path)
print("Uppercase Character Count:", uppercase_count)
