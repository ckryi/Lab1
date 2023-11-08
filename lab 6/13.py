def get_words_starting_with_vowel(words):

    vowel_words = []

    for word in words:
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_words.append(word)

    return vowel_words

words = ["apple", "banana", "orange", "bear", "cat"]
vowel_words = get_words_starting_with_vowel(words)
print(vowel_words)