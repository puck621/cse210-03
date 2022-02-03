import random

class Word:
    def __init__(self):
        my_file = open("game/word_list.txt", "r")
        dataString = my_file.read()
        self.wordlist = dataString.split("\n")
        print(self.wordlist)
        print(len(self.wordlist))

    def get_Word(self):
        return self.wordlist[random.randint(0, len(self.wordlist)-1)]
