# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
# print (wordlist)
#select random word from the list:
word = random.choice (wordlist)
print (word)
#welcome and start game
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is " ,len(word) , "letters long")

available  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guess = 8 
letter_list = list(word)
# print (letter_list)
# assert False
guessed = ''
seperator = ''
not_finished = True
while (not_finished):
    result = ''
    print ("You have " ,guess ,"guesses left" )
    print("Available letters :",seperator.join(available))
    user_guess = input("Please guess a letter: ")
    guessed += user_guess
    for char in letter_list:
        if char in guessed:
            result += char
        else:
            result += '_ '
        # print ( 'Oops! You\'ve already guessed that letter: ' ,)
    guess -= 1
    print ("Good guess: ",result)
    print (' _ '*12)
    available.remove(user_guess)
    if result == word:
        not_finished = False
print ("Congratuations, you won!")
    # print (available)
# your code begins here!
