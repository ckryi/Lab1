def correct_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        corrected_content = content.replace('B', 'J')
    return corrected_content

file_path = 'file9.txt'
corrected_content = correct_content(file_path)
print("Corrected Content:", corrected_content)
