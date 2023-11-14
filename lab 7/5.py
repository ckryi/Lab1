def count_words_ending_with_f(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words_ending_with_f = [word for word in content.split() if word.lower().endswith('f')]
        count = len(words_ending_with_f)
    return count

file_path = 'file5.txt'
count = count_words_ending_with_f(file_path)
print("Words ending with 'F' count:", count)
