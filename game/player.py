class Player:
    """
    the person playing the game
    the job of player is to keep track of the number of lives and the number of attempts the player has to guess the correct word
    
    """
    def __init__(self):
        
        """Defines all attributes
    
    Attributes:
        lives:  number of lives a player has left
        attempts: number of guesses the player has made
        correct_counter: number of correct guesses the player has made
        guesses: list of letters the player has guessed"""
            
        self.lives = 5
        self.attempts = 0
        self.correct_counter = 0
        self.guesses = []

    def wrong_attempt(self):
       """Removes a player life for each wrong guess
    
    Attributes:
        lives:  number of lives a player has left"""
        
        self.lives -= 1
        self.attempts += 1
    
    def get_lives(self):
        """Returns the number of lives for other classes
    
        Attributes:
        lives:  number of lives a player has left"""
        return self.lives
