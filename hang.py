import random
import string

WORDLIST_FILENAME = "palavras.txt"
NUM_CHANCES = 8


class SecretWord():
    def __init__(self, word):
        self.word = word
        self.numOfLetters = len(word)
        self.notFoundLetters = set(self.word)
        self.foundLetters = set()

    @property
    def numOfNotFoundLetters(self):
        return len(self.remainLetters)

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
        print('Available letters', self.attemptedLetters - self.acceptedLetters)

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
            if secretWord.numOfNotFoundLetters > self.chancesRemaing or chancesRemaing == 0:
                self.gameOver = True

    def printResultOfEvaluate(self, lettersLeft, wordFound):
        print(self.message, wordFound)
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
        self.wordlist = line.split()
        print(len(self.wordlist), "words loaded.")


def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    inFile.close()
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'
    return guessed


def getAvailableLetters(lettersGuessed):
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    return available


def hangman(secretWord):
    guesses = NUM_CHANCES
    lettersGuessed = []

    print('Welcome to the game of Hangam!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print('You have', guesses, 'guesses left.')
        available = getAvailableLetters(lettersGuessed)

        print('Available letters', available)
        letter = input('Please guess a letter: ')

        if letter in lettersGuessed:
            message = 'Oops! You have already guessed that letter: '

        elif letter in secretWord:
            lettersGuessed.append(letter)
            message = 'Good Guess: '

        else:
            guesses -= 1
            lettersGuessed.append(letter)
            message = 'Oops! That letter is not in my word: '

        guessed = getGuessedWord(lettersGuessed)
        print(message, guessed)
        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was', secretWord, '.')


wordlist = loadWords()
secretWord = random.choice(wordlist)
hangman(secretWord)
