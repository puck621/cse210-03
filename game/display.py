class Display:
    def __init__(self, word, player):
        self.word = word
        self.player = player
        self.length = len(word)
        self.letters = []

    def display_word(self):
        print(" ".join([letter if letter in self.letters else "_" for letter in self.word]))
        # Equivalent to:
        # for letter in self.word:
        #     if letter in self.letters:

        #         print(letter+ " ", end = "",flush = True)
        #     else:
        #         print("_ ", end = "", flush = True)
        # print()
     
    def display_person(self):
        print()
        if self.player.get_lives() > 4:
            print(" ___ ")

        if self.player.get_lives() > 3:
            print("/   \\")

        if self.player.get_lives() > 2:
            print("\   /")

        if self.player.get_lives() > 1:
            print(" \ / ")
            
        if self.player.get_lives() > 0:
            print("  O  ")

        if self.player.lives == 0:
            print("  X  ")

        print(" /|\ ")
        print(" / \ ")
        print("^^^^^^^")    


    def foundLetter(self, letter):
        self.letters.append(letter)