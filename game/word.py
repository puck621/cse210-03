import random

class Word:
    def __init__(self):
        with open("./game/word_list.txt", "r") as my_file:
            self.wordlist = my_file.readlines()

    def get_word(self):
        return random.choice(self.wordlist)
