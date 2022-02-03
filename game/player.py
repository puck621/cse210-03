class Player:
    def __init__(self):
        self.lives = 5
        self.guesses = []

    def wrong_attempt(self):
        self.lives -= 1

    def __str__(self):
        str_ = ""
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
    
        return str_