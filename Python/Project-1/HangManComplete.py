# Problem Set 2, hangman.py
# Name: Brian Saxon
# Collaborators: Brian Saxon
# Time spent: 8 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "D:\Code\Python\Project 1\words.txt"


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
    """+
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
    #Check through secret word to see if letter is in word or not.
    for letter in secret_word:
        if letter in letters_guessed:
            return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    n = ''
    #turn unguessed letters into underscores
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
    #Check if letter is guessed yet or not, if is, then removed from string showing available letters.
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
    invalid_guess = 3
    vowels = set("aeiou")
    print("I'm thinking of a word that is", len(secret_word), 'letters long.')
    print("You have 3 warnings.")
    print('---------------------')
    #loop till mistake points hit the limit to lose, or till the word is guessed to win
    while mistake_points < 6 and not is_word_guessed(secret_word, letters_guessed):
        print('You have ' + str(mistake_points) + '/6 guesses left.\nAvailable letters:', get_available_letters(letters_guessed))
        print("The word guessed so far is: " + get_guessed_word(secret_word, letters_guessed))
        current_guess = input('Please guess a letter or guess the whole word:').lower()
        #Check if guess is guess is a single character or word guess.
        if len(current_guess) <= 1:
                if current_guess in string.ascii_lowercase and current_guess != '':
                    #check if letter has been guessed yet.
                    if current_guess not in letters_guessed:
                        letters_guessed.append(current_guess)
                        #If letter is in word.
                        if current_guess in secret_word:
                            print("Good Guess:", end=' ')
                        #If letter is vowel and not in word
                        elif current_guess in vowels:
                            mistake_points +=2
                            print("Sorry, that vowel is not in this word. You lose 2 guesses")
                        #If letter is not vowel and not in word.
                        else:
                            mistake_points+=1
                            print("Nope! That letter is not in the word: ", end=' ')
                    #If letter had already been guessed
                    else:
                        invalid_guess -= 1
                        print("woopsie! That letter has already been guessed. You have " + str(invalid_guess) + " warnings left:", end= ' ')
                #If input isn't valid guess character
                else:
                    invalid_guess -= 1
                    print("woopsie! That is not a valid letter. You have ", str(invalid_guess) + " warnings left:", end= ' ')
       #Once loops is broken, win or not correct word guess
        else:
            if is_word_guessed(secret_word, list(current_guess)) and len(current_guess) == len(secret_word):
                letters_guessed = list(current_guess)
                print("You've guessed the word correctly!")
            else:
                mistake_points += 1
                print("Nope! That isn't the word I was thinking of:", end= ' ')
                print(get_guessed_word(secret_word,letters_guessed))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #winning statement with score
    if is_word_guessed(secret_word, letters_guessed):
        score = (6 - mistake_points) * (len((secret_word)))
        print("~~~WONDERFUL!~~~ You've won!\nYour final score for this game is: " + str(score))
    #Losing statement and reveal of word.
    else:
        print("Welp... Looks like you ran out of guesses. The word we were looking for was", secret_word)

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
    my_word_stripped = my_word.replace(" ", "")
    length = len(my_word_stripped)
    letters_my_word = list(my_word_stripped)
    #If lengths of words match look for same characters at indexes in the words.
    if len(other_word) == length:
        #Loops through to find matching characters or to dismiss underscores and continue looping to find chars.
        for i in range(length):
            if my_word_stripped[i] == other_word[i]:
                continue
            #If my_word has underscores, allow loop to continue without finding nothing.
            elif my_word_stripped[i] == "_" and other_word[i] not in letters_my_word:
                continue
            else:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    #Check through wordlist for possible matches using match_match_with_gaps
    for other_word in wordlist:
        #If match is found add the word to possible matches, else, continue to either show no match message, or show matches
        if match_with_gaps(my_word,other_word):
            possible_matches += (other_word + " ")
        else:
            continue
    if possible_matches == "":
        print("No Matches found")

    else:
        print(possible_matches)


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
    print("Welcome to Python Hangman! Now WITH hints!")
    print("The word to guess has " + str(len(secret_word)) + " letters long")
    print("You have a total of 6 guesses.")
    letters_guessed = []
    mistake_points = 0
    invalid_guess = 3
    vowels = set("aeiou")
    print("I'm thinking of a word that is", len(secret_word), 'letters long.')
    print("You have 3 warnings.")
    print('---------------------')
    # loop till mistake points hit the limit to lose, or till the word is guessed to win
    while mistake_points < 6 and not is_word_guessed(secret_word, letters_guessed):
        print('You have ' + str(mistake_points) + '/6 guesses left.\nAvailable letters:',
              get_available_letters(letters_guessed))
        print("The word guessed so far is: " + get_guessed_word(secret_word, letters_guessed))
        current_guess = input('Please guess a letter or guess the whole word:').lower()
        if len(current_guess) <= 1:
            #only difference from game wihthout hint! This is to check if player is asking for hint with * symbol
            if current_guess == '*':
                #Prints the list of possible mathces. If no matches found, then statement is also shown.
                print(show_possible_matches(get_guessed_word(secret_word,letters_guessed)))
            else:
                if current_guess in string.ascii_lowercase and current_guess != '':
                    if current_guess not in letters_guessed:
                        letters_guessed.append(current_guess)
                        if current_guess in secret_word:
                            print("Good Guess:", end=' ')
                        elif current_guess in vowels:
                            mistake_points += 2
                            print("Sorry, that vowel is not in this word. You lose 2 guesses")
                        else:
                            mistake_points += 1
                            print("Nope! That letter is not in the word: ", end=' ')
                    else:
                        invalid_guess -= 1
                        print("woopsie! That letter has already been guessed. You have " + str(
                            invalid_guess) + " warnings left:", end=' ')
                else:
                    invalid_guess -= 1
                    print("woopsie! That is not a valid letter. You have ", str(invalid_guess) + " warnings left:", end=' ')
        else:
            if is_word_guessed(secret_word, list(current_guess)) and len(current_guess) == len(secret_word):
                letters_guessed = list(current_guess)
                print("You've guessed the word correctly!")
            else:
                mistake_points += 1
                print("Nope! That isn't the word I was thinking of:", end=' ')
                print(get_guessed_word(secret_word, letters_guessed))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if is_word_guessed(secret_word, letters_guessed):
        score = (6 - mistake_points) * (len((secret_word)))
        print("~~~WONDERFUL!~~~ You've won!\nYour final score for this game is: " + str(score))
    else:
        print("Welp... Looks like you ran out of guesses. The word we were looking for was", secret_word)

    print("End of Game")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
