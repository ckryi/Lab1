def get_words_from_string(string):

    words = string.split()

    return words

input_string = "This is a string with several words."
words_list = get_words_from_string(input_string)
print(words_list)