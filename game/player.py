class Player:
    def __init__(self):
        self.lives = 5
        self.guesses = []

    def wrong_attempt(self):
        self.lives -= 1

    def get_lives(self):
        return self.lives
    
    def __str__(self) -> str:
        str_ = ""
        if self.get_lives() > 4:
            str_ += "\n  ___ \n"

        if self.get_lives() > 3:
            str_ += " /___\\\n"

        if self.get_lives() > 2:
            str_ += " \   /\n"

        if self.get_lives() > 1:
            str_ += "  \ / \n"
            
        if self.get_lives() > 0:
            str_ += "   O  \n"

        if self.lives == 0:
            str_ += "   X  \n"

        str_ += "  /|\ \n"
        str_ += "  / \ \n"
        str_ += "^^^^^^^\n"
        return str_
