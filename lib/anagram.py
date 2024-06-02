# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, word_array):
        self.word_array = word_array
        anagrams = []
        sorted_word = sorted(self.word)  # Sort the word once

        for w in word_array:
            if sorted(w.lower()) == sorted_word:  # Convert each word to lowercase for comparison
                anagrams.append(w)

        return anagrams
