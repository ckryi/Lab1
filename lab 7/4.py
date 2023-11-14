def count_lines_not_starting_with_d(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        count = sum(1 for line in lines if not line.strip().startswith('D'))
    return count

file_path = 'file4.txt'
line_count = count_lines_not_starting_with_d(file_path)
print("Number of lines not starting with 'D':", line_count)
