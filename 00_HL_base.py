import math
import random


# Functions go here

# statement decoration types
def statement_decorator(statement, decoration, dec_type):
    # Set decoration length
    sides = decoration * 5

    # set decoration types
    # add decoration to start and ent of statement
    if dec_type == "s":
        statement = "{} {} {}".format(sides, statement, sides)
        print(statement)
    # add decoration to top and bottom of statement
    elif dec_type == "tb":
        tb_dec = decoration * len(statement)
        print(tb_dec)
        print(statement)
        print(tb_dec)
    # add decoration all around statement
    else:
        statement = "{} {} {}".format(sides, statement, sides)
        tb_dec = decoration * len(statement)
        print(tb_dec)
        print(statement)
        print(tb_dec)

    return ""


# checks user response is yes/no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        response = response.replace(" ", "")

        if response == "yes" or response == "y":
            response = "yes"
            return response

            # If they say no, output 'display instructions'

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Displays instructions
def instructions():
    statement_decorator("How to Play", "*", "s")

    print("\nEach game you will be asked to enter a 'High' or 'Low' Number")
    print("A 'secret' number will be picked between those two numbers")
    print("\n-Guess a number to try and find the secret number.")
    print("  The amount of guesses you have depends on your 'high' and 'low' number. ")
    print("-Each time you guess a number, you will be told if it is higher or lower\n  than the secret number.")
    print("\nPress 'xxx' at any time to end the game")
    print("\nHave fun!")
    print()
    return ""


# Get the high and low numbers for the number range, also round check
def int_check(question, low=None, high=None, exit_code=None):
    situation = ""

    # if low and high
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        response = input(question)
        if exit_code is not None:
            if response == "":
                return response

        try:
            response = int(response)

            # checks guess input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}.")
                    continue

            # checks high number is not too low
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is higher than (or equal to) {low}")
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter a integer. ")
            continue


# Main routine goes here

# Game Title
print()
statement_decorator("Welcome to Higher or Lower", "*", "s")

# ask if the user would like to see the instructions
print()
see_instructions = yes_no("Would you like to see the instructions? ")
print()
if see_instructions == "yes":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0

# initialise lost and win counters
rounds_won = 0
rounds_lost = 0

mode = "regular"

# Ask user for # of rounds, <enter> for indefinite mode
rounds = int_check("How many rounds?: ", 1, exit_code="xxx")
if rounds == "":
    mode = "infinite"
    rounds = 5

# Set up list for game stats
game_summary = []

# Ask user for choice and check that it's valid
end_game = "no"
while end_game == "no":

    # Start of gameplay loop

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        rounds += 1

    else:
        heading = f"Round of {rounds_played + 1} of {rounds}"

    print(heading)
    # get the range the secret number is between

    lowest = int_check("Low number: ")
    highest = int_check("High Number: ", lowest + 1)

    # get the secret number
    secret_num = random.randint(lowest, highest)

    # calculate the number of guesses allowed
    guess_range = highest - lowest + 1
    max_raw = math.log2(guess_range)
    max_upped = math.ceil(max_raw)
    guesses_allowed = max_upped + 1
    print(f"Max Guesses: {guesses_allowed}")
    guesses_left = guesses_allowed

    # set list to prevent duplicates
    already_guessed = []

    # get users guess
    guess = int_check("Guess a number: ", lowest, highest)

    # compare numbers
    while guess != secret_num and guesses_left >= 1:

        guess = int(input("Guess: "))  # replace this with function

        # checks that guess is not a duplicate
        if guess in already_guessed:
            print(f"You already guessed that number! Please try again. You *still* have {guesses_left} guesses left")
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:
            if guess < secret_num:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > secret_num:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

        else:
            if guess < secret_num:
                print("Too low!")
            elif guess > secret_num:
                print("Too high!")

    if guess == secret_num:
        if guesses_left == guesses_allowed - 1:
            print(f"Amazing! You got it in one!")
        else:
            print(f"Well done. You got it in {len(already_guessed)}.")
        rounds_won += 1

    elif guesses_left == 0:
        print("Better luck next time.")
