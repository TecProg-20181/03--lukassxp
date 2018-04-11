import random
import string

WORDLIST_FILENAME = "words.txt"
NUM_CHANCES = 8


class SecretWord():
    def __init__(self, word):
        self.word = word
        self.numOfLetters = len(word)
        self.notFoundLetters = set(self.word)
        self.foundLetters = set()

    @property
    def numOfNotFoundLetters(self):
        return len(self.notFoundLetters)

    @property
    def wasWordFound(self):
        if self.numOfNotFoundLetters != 0:
            return False
        return True

    @property
    def wordFound(self):
        wordFound = ''
        for letter in self.word:
            if letter in self.foundLetters:
                wordFound += letter
            else:
                wordFound += '_'
        return wordFound


class AssistantOfHangman():
    def __init__(self):
        self.chancesRemaing = NUM_CHANCES
        self.attemptedLetters = set()
        self.acceptedLetters = set(string.ascii_lowercase)
        self.guess = ''
        self.result = ''
        self.gameOver = False
        self.wordList = []

    def isValidSecretWord(self, distinctLetters):
        if distinctLetters > NUM_CHANCES:
            return False
        return True

    @property
    def printAvaliableLetters(self):
        print('Available letters', sorted(self.acceptedLetters - self.attemptedLetters))

    def printWelcomeText(self, letters, distinctLetters):
        print('Welcome to the game of Hangam!')
        print('I am thinking of a word with', letters, 'in all and', distinctLetters, 'different letters.')

    @property
    def printChancesRemaing(self):
        print('You have', self.chancesRemaing, 'chances remaing.')

    @property
    def askGuess(self):
        self.guess = input('Please guess a letter: ')

    def evaluateGuess(self, secretWord):
        if self.guess in self.attemptedLetters:
            self.result = 'Oops! You have already guessed that letter: '
        elif self.guess in secretWord.notFoundLetters:
            secretWord.foundLetters.add(self.guess)
            secretWord.notFoundLetters.discard(self.guess)
            self.result = 'Good Guess: '
        else:
            self.attemptedLetters.add(self.guess)
            self.chancesRemaing -= 1
            self.result = 'Oops! That letter is not in my word: '
            if secretWord.numOfNotFoundLetters > self.chancesRemaing or self.chancesRemaing == 0:
                self.gameOver = True

    def printResultOfEvaluate(self, lettersLeft, wordFound):
        print(self.result, wordFound)
        print("Distinct letters remaining to discover: ", lettersLeft)

    @property
    def isGameOver(self):
        return self.gameOver

    @property
    def loadWordList(self):
        print("Loading word list from file...")
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        inFile.close()
        self.wordList = line.split()
        print(len(self.wordList), "words loaded.")


def hangman():
    assistant = AssistantOfHangman()
    assistant.loadWordList

    secretWord = SecretWord(random.choice(assistant.wordList))
    while not assistant.isValidSecretWord(secretWord.numOfNotFoundLetters):
        secretWord = secretWord = SecretWord(random.choice(assistant.wordList))

    assistant.printWelcomeText(secretWord.numOfLetters, secretWord.numOfNotFoundLetters)
    print('-------------')

    while not secretWord.wasWordFound and not assistant.isGameOver:
        assistant.printChancesRemaing
        assistant.printAvaliableLetters
        assistant.askGuess
        assistant.evaluateGuess(secretWord)
        assistant.printResultOfEvaluate(secretWord.numOfNotFoundLetters, secretWord.wordFound)
        print('------------')
    else:
        if secretWord.wasWordFound:
            print('Congratulations, you won!')
        elif assistant.chancesRemaing != 0:
            print('Sorry, but you do not have enough chastity to guess the missing letters of the word.')
            print('The word was', secretWord.word)
        else:
            print('Sorry, you ran out of guesses. The word was', secretWord.word)


hangman()
