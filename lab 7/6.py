def count_all_none_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        all_count = content.lower().count('all')
        none_count = content.lower().count('none')
    return all_count, none_count

file_path = 'file6.txt'
all_count, none_count = count_all_none_words(file_path)
print("Count of 'all':", all_count)
print("Count of 'none':", none_count)
