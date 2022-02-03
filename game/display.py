from game.word import Word
from game.player import Player

class Display:
    def __init__(self, word, player):
        self.word = word
        if self.lives == 5:
            str_ += "  ___ \n"

        if self.lives == 4:
            str_ += " /___\\\n"

        if self.lives == 3:
            str_ += " \   /\n"

        if self.lives == 2:
            str_ += "  \ / \n"
            
        if self.lives == 1:
            str_ += "   O  \n"

        if self.lives == 0:
            str_ += "  X  \n"

        str_ += " /|\ \n"
        str_ += " / \ \n"
        str_ += "^^^^^\n"