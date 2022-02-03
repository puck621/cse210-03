import random
import sys

class Game:
    def __init__(self):
        self.still_playing = ""
        self.player = Player()
        self.word = Word()
        self.secret_word = words.get_word()
        self.display = Display(secrect_word, player)
        
       
    def main(self):
        still_playing = True
        while player.lives > 0 and keepGoing == True:
            guess = input("Guess a letter [a-z] or type "quit" to quit: ")
            while len(guess) > 1:
                print("Please only input one letter")
                guess = input("Guess a letter [a-z]: ")
                print("You guessed: ", guess)
            if guess == "quit":
                still_playing = False
                print("The secret word is ", secrect_word)
                break
            for letter in theword:
                if letter == guess:
                    display.foundLetter(letter)
                    display.display_word()
                    display.diplay_person
        







    

if __name__ == "__main__":
    game = Game()
    game.start_game()