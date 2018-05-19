import random
import string

WORDLIST_FILENAME = "words.txt"
NUM_CHANCES = 8


class SecretWord():
    def __init__(self, word):
        self._word = self.validSecretWord(word=word)
        self._numOfLetters = len(word)
        self._notFoundLetters = set(self._word)
        self._foundLetters = set()

    def validSecretWord(self, word):
        if not word.isalpha():
            print('Error, the load choice from archive contains',
                  'non alphabethic characters. Ending execution.')
            exit()
        else:
            return word.lower()

    @property
    def word(self):
        return self._word

    @property
    def foundLetters(self):
        return self._foundLetters

    @property
    def notFoundLetters(self):
        return self._notFoundLetters

    @property
    def numOfLetters(self):
        return self._numOfLetters

    @property
    def numOfNotFoundLetters(self):
        return len(self._notFoundLetters)

    @property
    def wasWordFound(self):
        return (False if not self.numOfNotFoundLetters == 0 else True)

    @property
    def wordFound(self):
        wordFound = ''
        for letter in self._word:
            wordFound += (letter if letter in self._foundLetters else '_')

        return wordFound


class AssistantOfHangman():
    def __init__(self):
        self._chancesRemaing = NUM_CHANCES
        self._attemptedLetters = set()
        self._acceptedLetters = set(string.ascii_lowercase)
        self._guess = ''
        self._result = ''
        self._gameOver = False
        self._wordList = []

    @property
    def wordList(self):
        return self._wordList

    def isValidTamSecretWord(self, distinctLetters):
        return (False if distinctLetters > NUM_CHANCES else True)

    @property
    def printAvaliableLetters(self):
        temp = sorted(self._acceptedLetters - self._attemptedLetters)
        print('Not attempted letters: ', ''.join(i + ' - ' for i in temp))

    def printWelcomeText(self, letters, distinctLetters):
        print('Welcome to the game of Hangam!')
        print('I am thinking of a word with', letters,
              'in all and', distinctLetters, 'different letters.')

    @property
    def printChancesRemaing(self):
        print('You have', self._chancesRemaing, 'chances remaing.')

    @property
    def askGuess(self):
        self._guess = input('Please guess a letter: ').lower()
        if self._guess not in self._acceptedLetters:
            print("Invalid input!")
            self.askGuess

    def evaluateGuess(self, notFoundLetters, foundLetters):
        if self._guess in self._attemptedLetters:
            self._result = 'Oops! You have already guessed that letter: '
        elif self._guess in notFoundLetters:
            foundLetters.add(self._guess)
            notFoundLetters.discard(self._guess)
            self._attemptedLetters.add(self._guess)
            self._result = 'Good Guess: '
        else:
            self._attemptedLetters.add(self._guess)
            self._chancesRemaing -= 1
            self._result = 'Oops! That letter is not in my word: '
            if self._chancesRemaing == 0:
                self._gameOver = True

    def printResultOfEvaluate(self, lettersLeft, wordFound):
        print(self._result, wordFound)
        print("Distinct letters remaining to discover: ", lettersLeft)

    @property
    def isGameOver(self):
        return self._gameOver

    @property
    def loadWordList(self):
        print("Loading word list from file...")

        try:
            inFile = open(WORDLIST_FILENAME, 'r')
            line = inFile.readline()
            inFile.close()
        except IOError:
            print("Occured one error during the archive",
                  "manipulation. Ending execution.")
            exit()
        else:
            self._wordList = line.split()
            temp = len(self._wordList)
            if temp is 0:
                print('None word found in archive, ending execution.')
                exit()
            print(temp, 'words loaded.')


def hangman():
    assistant = AssistantOfHangman()
    assistant.loadWordList

    secretWord = SecretWord(random.choice(assistant.wordList))
    while not assistant.isValidTamSecretWord(secretWord.numOfNotFoundLetters):
        secretWord = SecretWord(random.choice(assistant.wordList))

    assistant.printWelcomeText(letters=secretWord.numOfLetters,
                               distinctLetters=secretWord.numOfNotFoundLetters)
    print('-------------')

    while not secretWord.wasWordFound and not assistant.isGameOver:
        assistant.printChancesRemaing
        assistant.printAvaliableLetters
        assistant.askGuess
        assistant.evaluateGuess(notFoundLetters=secretWord.notFoundLetters,
                                foundLetters=secretWord.foundLetters)
        assistant.printResultOfEvaluate(lettersLeft=secretWord.numOfNotFoundLetters,
                                        wordFound=secretWord.wordFound)
        print('------------')
    else:
        if secretWord.wasWordFound:
            print('Congratulations, you won!')
        elif assistant.isGameOver:
            print('Sorry, you ran out of guesses. The word was',
                  secretWord.word)


hangman()
