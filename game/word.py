import random

class Word:
    """Chooses a random word to be guessed by the player from the list of words in the word list"""
    def __init__(self):
        with open("./game/word_list.txt", "r") as my_file:
            self.wordlist = my_file.readlines()

    def get_word(self):
        return random.choice(self.wordlist).lower()
