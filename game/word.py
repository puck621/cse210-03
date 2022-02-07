import random

class Word:
    def __init__(self):
        with open("./game/word_list.txt", "r") as my_file:
            self.wordlist = my_file.readlines()
            print(self.wordlist[:10])
        self.letters = []
        self.word = random.choice(self.wordlist).strip().lower()

    def found_letter(self, letter):
        self.letters.append(letter)
    
    def __str__(self) -> str:
        return " ".join([letter if letter in self.letters else "_" for letter in self.word])