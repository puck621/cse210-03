import random

class Word:
    """Chooses a random word to be guessed by the player from the list of words in the word list"""
    def __init__(self):
     """Imports full word list from the scrabble template
    
        Attributes:
        wordlist: all available words"""  
        
        with open("./game/word_list.txt", "r") as my_file:
            self.wordlist = my_file.readlines()

    def get_word(self):
        
       """Returns random word from full list of scrabble words
    
        Attributes:
        wordlist: all available words"""  
        
        return random.choice(self.wordlist).lower()
