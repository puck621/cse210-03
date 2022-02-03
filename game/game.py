from game.word import Word
from game.player import Player

class Game:
    def __init__(self):
        self.still_playing = ""
        self.player = Player()
        self.word = Word()
               
    def main(self):
        still_playing = True
        while self.player.lives > 0 and still_playing == True:
            guess = input("Guess a letter [a-z] or type q to quit: ")
            while len(guess) > 1:
                print("Please only input one letter")
                guess = input("Guess a letter [a-z]: ")
                print("You guessed: ", guess)
            if guess == "q":
                still_playing = False
                print("The secret word is ", self.word.word)
                break
            for letter in theword:
                if letter == guess:
                    # Placeholder for correct guesses
                    # Placeholder for printing the word
                    print(self.player)
        

if __name__ == "__main__":
    game = Game()
    game.start_game()