# Problem Set 2, hangman.py
# Name: Brian Saxon
# Collaborators: Brian Saxon
# Time spent: 2 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
word = choose_word(wordlist)
secret_word = list(word)
guessed = []


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        else:
            return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    n = ''
    for char in secret_word:
        n += (char if char in letters_guessed else '_ ')
    return n


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns1: string (of letters), comprised of letters that represents which letters have not
      yet b12een guessed.
    '''
    all_letters = string.ascii_lowercase
    av_let = ''
    for char in all_letters:
        if not (char in letters_guessed):
            av_let += char
    return av_let


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to Python Hangman!')
    print("The word to guess has " + str(len(secret_word))+ " letters long")
    print("You have a total of 6 guesses.")
    letters_guessed = []
    mistake_points = 0
    while mistake_points < 6:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if not is_word_guessed(secret_word, letters_guessed):
            print("Letters available to guess: " + get_available_letters(letters_guessed))
            invalid_guess = 3
            print("Here is the word so far: ")
            print(get_guessed_word(secret_word, letters_guessed))
            while True:
                if invalid_guess !=1:
                    current_guess = str.lower(input("What is your guess? " + str(mistake_points)+"/6 guesses used: "))
                    if len(current_guess) !=1:
                        print("Please type 1 letter at a time.")
                        invalid_guess -= 1
                        print("You have" + str(invalid_guess) + " chances left to enter a valid guess.")

                    elif current_guess not in string.ascii_lowercase:
                        print("This is not a lowercase letter")
                        invalid_guess -= 1
                        print("You have" + str(invalid_guess) + " chances left to enter a valid guess.")

                    elif current_guess in letters_guessed:
                        print("You have already guessed this letter")
                        invalid_guess -= 1
                        print("You have" + str(invalid_guess) + " chances left to enter a valid guess.")

                    else:
                        letters_guessed += current_guess
                        if current_guess in secret_word:
                            if not is_word_guessed(secret_word, letters_guessed):
                                print("Congratulations, you guessed a letter in the word")
                                print("Here is the word so far: ")
                                print(get_guessed_word(secret_word, letters_guessed))
                            else:
                                break
                        else:
                            print("This letter is not in the word!")
                            if current_guess in "aeiou":
                                mistake_points += 2
                                print("This was an incorrect vowel, you have last 2 guesses")
                            else:
                                mistake_points += 1
                                print("This was an incorrect consonant, you lose 1 guess.")
                            break
                else:
                    print("That was 3 errors, you have lost a guess!")
                    mistake_points += 1
                    break

        elif is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You have guessed the word!")
            print(get_guessed_word(secret_word, letters_guessed))
            unique_chars = ""
            score = (6 - mistake_points) * (len(unique_chars.join(set(secret_word))))
            print ("Your final score for this game is: " + str(score))
            break
        else:
            print("Woops! Looks like you ran out of guesses!")
            print("The word to guess was: " + str(secret_word))
    if mistake_points >=6:
        print("Woops! Looks like you ran out of guesses!")
        print("The word to guess was: " + str(secret_word))


    print("End of Game")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
