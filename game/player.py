class Player:
    def __init__(self):
        self.lives = 5
        self.attempts = 0
        self.correct_counter = 0
        self.guesses = []

    def wrong_attempt(self):
        self.lives = self.lives -1
        self.attempts = self.attempts + 1
    
    def get_lives(self):
        return self.lives