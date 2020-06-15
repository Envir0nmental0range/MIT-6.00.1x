# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    display = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            display += letter + ' '
        else:
            display += '_ '
    return(display)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    lettersString = string.ascii_lowercase
    availableLetters = ''
    for letter in lettersString:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to Hangman. Your word is ' + str(len(secretWord)) + ' characters long')
    turns = 1
    maximumTurns = 8
    lettersGuessed = ''
    mistakesMade = 0
    while turns <= maximumTurns and isWordGuessed(secretWord, lettersGuessed) == False:
        print('the following letters are available: ' + getAvailableLetters(lettersGuessed))        
        print('Turn number ' + str(turns) + ' of ' + str(maximumTurns) + '. You have made ' + str(mistakesMade) + ' error(s).')
        guessLetter = str(input('Enter one letter for your guess '))
        if guessLetter in lettersGuessed:
            print('You have already guessed the letter ' + str(guessLetter) + ' please enter another selection')
            continue
        elif guessLetter in secretWord:
            print('Congratulations! The letter ' + guessLetter + ' is part of the secret word.')
        else:
            print('Sorry! The letter ' + guessLetter + ' is  NOT part of the secret word.')
            mistakesMade += 1
        lettersGuessed += guessLetter
        print(getGuessedWord(secretWord, lettersGuessed))
        turns +=1
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print('Sorry, you have run out of turns, the correct answer was: ' + secretWord)
    else:
        print('Congratulations! You have correctly guessed the word: ' + secretWord)
        
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
#hangman('apple')
