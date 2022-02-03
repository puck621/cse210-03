class Word:
    def __init__(self):
        file = open(word_list.txt)
        dataString = file.read()
        self.wordlist = dataString.split("\n")

    def get_Word(self):
        return self.wordlist[random.randint(0, len(self.wordlist)-1)]