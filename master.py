import random

class Master:
    def __init__(self,words,maxGuesses):
        self.word = random.choice(words)
        self.guessesLeft = maxGuesses
        self.length = len(self.word)
        
    def getMatches(self,guess):
        if not self.guessesLeft: return 'Out of Guesses'
        self.guessesLeft -= 1
        
        matches = 0
        for i in range(self.length):
            matches += 1 if guess[i] == self.word[i] else 0
        
        return matches if matches < self.length else 'Found'
    
    def getGuessesLeft(self):
        return self.guessesLeft