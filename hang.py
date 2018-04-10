import random
import string

WORDLIST_FILENAME = "palavras.txt"


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    inFile.close()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return random.choice(wordlist)


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
    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')

    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print('You have ', guesses, 'guesses left.')
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
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')


secretWord = loadWords().lower()
hangman(secretWord)
