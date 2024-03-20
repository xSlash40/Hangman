# external library used to generate the random word
from wonderwords import RandomWord

attempts = 0
word = RandomWord().word(word_min_length=3, word_max_length=8)

# procedure 1 (defining how difficult the game will be)


def rules():
    global attempts
    difficulty = ""

    print("Which difficulty would you like to play the game in?")
    print("Easy (10 attempts) --> type '1'")
    print("Medium (5 attempts) --> type '2'")
    print("Hard (3 attempts) --> type '3'")

    difficulty = input("> ")

    match difficulty:
        case "1":
            attempts = 10
        case "2":
            attempts = 5
        case "3":
            attempts = 3


# print(word)
# procedure 2 (the actual hangman/word guesser game)
def guess_word():
    global attempts
    guessed_letters = 0
    print(f"The word is a {len(word)} letter word")

    while (attempts != 0) and (guessed_letters != len(word)):

        guess = input("Guess a letter > ")
        while (len(guess) > 1):
            print("Your guess has to be one letter")
            guess = input("Guess a letter > ")
        attempts = attempts - 1

        if (guess) in word:

            # list that stores postiions of the guessed letters
            positions = [i + 1 for i,
                         letter in enumerate(word) if letter == guess]

            guessed_letters = guessed_letters + 1

            print(
                f"Correct! Your guess is at position {positions} of the word")

        elif (guess) not in word:
            print(f"Incorrect! You have {attempts} attempts remaning")


# procedure 3 (the final stage of the hangman/word guesser game)
def final_guess():
    print("Now, guess the word!")
    final_guess = input("> ")

    if (final_guess == word):
        print("Yay! You guessed the word")
    elif (final_guess != word):
        print("You did not guess the word :/")
        print(f"The correct word was: {word}")


rules()
guess_word()
final_guess()
