class Display:
    """handles the display of the jumper status in the terminal"""
    
    def __init__(self, word, player):
            """Defines all attributes
    
    Attributes:
        player:  player playing the game
        word:   gets the random word for game play
        letters: list of letters for the secret word. Will show as _ and guessed letters"""
            
        self.word = word
        self.player = player
        self.letters = []

    def display_word(self):
            """ Displays the correct guessed letters and the blank spaces for unguessed letters
            
    Attributes:
         letters: list of letters for the s"""
        
        print(" ".join([letter if letter in self.letters else "_" for letter in self.word]))
        # Equivalent to:
        # for letter in self.word:
        #     if letter in self.letters:

        #         print(letter+ " ", end = "",flush = True)
        #     else:
        #         print("_ ", end = "", flush = True)
        # print()
     
    def display_person(self):
        """displays the jumper as the game progresses depending on the guess 
        of a correct or incorrect letter from the player"""
        
            """     
    Attributes:
        player:  player playing the game
        lives:   number of lives the player has left
"""
            
        print()
        if self.player.get_lives() > 4:
            print("  ___ ")

        if self.player.get_lives() > 3:
            print(" /___\\")

        if self.player.get_lives() > 2:
            print(" \   /")

        if self.player.get_lives() > 1:
            print("  \ / ")
            
        if self.player.get_lives() > 0:
            print("   O  ")

        if self.player.lives == 0:
            print("   X  ")

        print("  /|\ ")
        print("  / \ ")
        print("\n^^^^^^^")    

    def foundLetter(self, letter):
        
        """ Updates the list of letters for the displayed word if a letter is guessed correctly
            
        Attributes:
         letters: list of letters for the s"""
            
        self.letters.append(letter)
