class Player:
    def __init__(self):
        self.lives = 5
        self.guesses = []

    def wrong_attempt(self):
        self.lives -= 1
