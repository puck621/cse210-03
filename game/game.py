from game.word import Word
from game.player import Player

class Game:
    def __init__(self):
        self.still_playing: bool
        self.player = Player()
        self.word = Word()

    def main(self):
        self.still_playing = True
        while self.player.lives > 0 and self.still_playing == True:
            guess = input("Guess a letter [A-Z] or type quit to quit: ")
            guess = guess.lower()
            if guess in ["quit", "exit"]:
                self.still_playing = False
                continue
            elif len(guess) != 1:
                print("Please only input one letter")
                continue

            self.player.guesses.append(guess)
            print("You've guessed:", ", ".join(self.player.guesses))
            if guess in self.word.word:
                self.word.found_letter(guess)
                print("You found a letter!")
            else:
              self.player.wrong_attempt()

            if set(self.word.letters) == set(self.word.word):
                print("You won!")
                self.still_playing = False

            print(self.word)
            print(self.player)
        else:
            print("Game Over")
            print("The secret word is", self.word.word)
            


if __name__ == "__main__":
    game = Game()
    game.main()
