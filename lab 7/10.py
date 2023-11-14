def count_a_b_occurrences(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        a_count = content.lower().count('a')
        b_count = content.lower().count('b')
    return f'a={a_count}, b={b_count}'

file_path = 'file10.txt'
occurrences = count_a_b_occurrences(file_path)
print("Occurrences:", occurrences)
