# 6.00 Problem Set 3
# Hangman game
# Haoran WANG

# -----------------------------------


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    for letter in secretWord:
        if letter not in lettersGuessed[:]:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=''
    for letter in secretWord:
        if letter not in lettersGuessed:
            result=result+'_'
        elif letter in lettersGuessed:
            result=result+letter
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result2=''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result2=result2+letter
    return result2



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
    n=8
    lettersGuessed=[]
    TotalGuesses=[]
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long'
    print '-----------'
    while secretWord!=str(getGuessedWord(secretWord,lettersGuessed)):
        print 'You have '+str(n)+' guesses left'
        print 'Available letters: '+ str(getAvailableLetters(lettersGuessed))
        Guess=raw_input('please guess a letter:')
        lettersGuessed+=Guess
        availableLetters=getAvailableLetters(lettersGuessed)
        if Guess in secretWord:
            if Guess not in TotalGuesses:
                print 'Good guess: '+str(getGuessedWord(secretWord,lettersGuessed))
                print '-----------'
                TotalGuesses+=Guess
            elif Guess in TotalGuesses:
                print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord,lettersGuessed))
                print '-----------'
        elif Guess not in secretWord:
            if n>1:
                if Guess not in TotalGuesses:
                    print 'Oops! That letter is not in my word: '+str(getGuessedWord(secretWord,lettersGuessed))
                    print '-----------'
                    n=n-1
                    TotalGuesses+=Guess
                elif Guess in TotalGuesses:
                    print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord,lettersGuessed))
                    print '-----------'
            elif n<=1:
                print 'Oops! That letter is not in my word: '+str(getGuessedWord(secretWord,lettersGuessed))
                print '-----------'
                return 'Sorry, you ran out of guesses. The word was str(secretWord).'
    return 'Congratulations, you won!'

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
