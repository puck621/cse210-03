import random
import sys

class Game:
    def __init__(self):

       
    def main(self):
        player = Player()
        word = Word()
        secret_word = words.get_word()
        display = Display(secrect_word, player)
        keepGoing = True
        print("the Word is", secrect_word)
        while player.lives > 0 and keepGoing == True:
            guess = input("Guess a letter [a-z] or input ! to quit: ")
            while len(guess) > 1:
                print("Please only input one letter")
                guess = input("Guess a letter [a-z]: ")
                print("your input was ", guess)
            if guess == "!":
                keepGoing = False
                break
            for letter in theword:
                if letter == guess:
                    display.foundLetter(letter)
                    display.display()
        







    

if __name__ == "__main__":
    game = Game()
    game.start_game()