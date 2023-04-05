import math
import random


# Functions go here

# statement decoration types
def statement_decorator(statement, decoration):
    # Make string with three characters
    sides = decoration * 5

    # add decoration to start and ent of statement
    statement = "{} {} {}".format(sides, statement, sides)
    print(statement)

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
    statement_decorator("How to Play", "*")

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
            elif response == exit_code:
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
statement_decorator("Welcome to Higher or Lower", "*")

# ask if the user would like to see the instructions
replay_game = "yes"
while replay_game == "yes":
    print()
    see_instructions = yes_no("Would you like to see the instructions? ")
    print()
    if see_instructions == "yes":
        instructions()

    # get the range the secret number is between
    lowest = int_check("Low number: ")
    highest = int_check("High Number: ", lowest + 1)

    # Ask user for # of rounds then loop...
    rounds_played = 0

    # initialise lost and win counters
    rounds_won = 0
    rounds_lost = 0

    mode = "regular"

    # Ask user for # of rounds, <enter> for indefinite mode
    mode_valid = "no"
    while mode_valid == "no":
        rounds = int_check("How many rounds?: ", 1, None, "xxx")
        if rounds == "":
            mode = "infinite"
            rounds = 5
            break
        elif rounds == "xxx":
            print()
            continue
        else:
            break

    # Set up lists for game stats
    game_summary = []
    round_score = []

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

        # get the secret number
        secret_num = random.randint(lowest, highest)
        print(secret_num)

        # calculate the number of guesses allowed
        guess_range = highest - lowest + 1
        max_raw = math.log2(guess_range)
        max_upped = math.ceil(max_raw)
        guesses_allowed = max_upped + 1
        print(f"Max Guesses: {guesses_allowed}")
        guesses_left = guesses_allowed

        # set list to prevent duplicates
        already_guessed = []

        # compare numbers
        # get users guess
        guess = int_check("Guess a number: ", lowest, highest, "xxx")

        # End game if exit code is typed
        if guess == "xxx":
            break

        # checks that guess is not a duplicate
        elif guess in already_guessed:
            print(f"You already guessed that number! Please try again. You *still* have {guesses_left} guesses left")
            continue

        elif guess != secret_num:

            guesses_left -= 1
            already_guessed.append(guess)

            # check if the guess is lower or higher than the secret number, then tell the user
            if guess < secret_num:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))
            elif guess > secret_num:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

        # if the guess is the same as the secret number, the user wins
        elif guess == secret_num:
            if guesses_left == guesses_allowed:
                # custom message if the got it in one
                print(f"Amazing! You got it in one!")
            else:
                print(f"Well done. You got it in {len(already_guessed) + 1}.")
            rounds_won += 1
            result = "Win"

        # if the number of guesses left is less than one, the user lost
        elif guesses_left < 1:
            print("Better luck next time.")
            rounds_lost += 1
            result = "Loss"

        # if the number of rounds played equals the amount of rounds, end game
        if rounds_played == rounds:
            break
        else:
            continue

    print()
    replay = yes_no("Would you like to play again?: ")
    if replay == "yes":
        continue
    else:
        break

print()
print("Thank you for playing!!")
