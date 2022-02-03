from game.word import Word
from game.player import Player
from game.display import Display

class Game:
    def __init__(self):
        self.still_playing = ""
        self.player = Player()
        self.word = Word()
        self.secret_word = self.word.get_Word()
        self.display = Display(self.secret_word, self.player)

    def main(self):
        #For testing remove for real play
        print("The secret word is ", self.secret_word)

        self.still_playing = True
        while self.player.lives > 0 and self.still_playing == True:
            guess = input("Guess a letter [A-Z] or type quit to quit: ")
            guess = guess.upper()
            if guess == "quit":
                self.still_playing = False
                print("The secret word is ", self.secret_word)
                break
            elif len(guess) != 1:
                print("Please only input one letter")
                continue

            print("You guessed: ", guess)
            for letter in self.secret_word:
                found = False
                if letter == guess:
                    self.display.foundLetter(letter)
                    found = True
                    break

            if not found:
              self.player.wrong_attempt()

            self.display.display_word()
            self.display.display_person()


if __name__ == "__main__":
    game = Game()
    game.start_game()
