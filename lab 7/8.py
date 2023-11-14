def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
    return longest_word

file_path = 'file8.txt'
longest_word = find_longest_word(file_path)
print("Longest Word:", longest_word)