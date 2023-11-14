from collections import Counter

def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_frequency = Counter(words)
    return word_frequency

file_path = 'file7.txt'
frequency = count_word_frequency(file_path)
print("Word Frequency:", frequency)
