import random

class Word:
    # Creating atrributes for the class.
    def __init__(self):
        # Opening file for the program to read.
        with open("wordBank.txt", "rt") as infile:
            self.list_of_words = infile.readlines()

    # Chooses a word from the word bank file.
    def get_word(self):
        random_word = random.choice(self.list_of_words)
        return random_word

    # Creates a list from the selected word.
    def list_word(self):
        letter_list = list(self.random_word)

    # Hiding the word from the user
    def secretWord(self, letter_list):
        blanks = ['_ '] * len(letter_list)
        return blanks