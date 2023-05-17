import math
import random


# Functions go here

# statement decoration types
def statement_decorator(statement, decoration):
    # Make string with five characters
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

        # If the response is valid, return response
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        # If not, print error
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


# Check if a number is an Integer within specified bounds
def int_check(question, low=None, high=None, exit_code=None):

    # set the situation depending on what parameters were entered
    if low is not None and high is not None:
        situation = "both"
        error = f"Please enter an integer between {low} and {high}"
    elif low is not None and high is None:
        situation = "low only"
        error = f"Please enter a number that is higher than (or equal to) {low}"
    else:
        situation = "any integer"
        error = "Please enter an integer"

    while True:

        # Allow "" and the exit code to be a valid input
        response = input(question)
        if exit_code is not None:
            if response == "":
                return response
            if response == exit_code:
                return response

        try:
            response = int(response)

            # checks guess input is not too high or low if both upper and lower bounds are specified
            if situation == "both":
                if low <= response <= high:
                    return response

            # checks if a number is higher than low if only lower bounds are specified
            elif situation == "low only":
                if response >= low:
                    return response

            else:
                return response

            print(error)

        # If input it not an integer, print error and ask question again
        except ValueError:
            print(error)
            continue


# Main routine goes here

# Game Title
print()
statement_decorator("Welcome to Higher or Lower", "*")

# ask if the user would like to see the instructions
print()
see_instructions = yes_no("Would you like to see the instructions? ")
print()
if see_instructions == "yes":
    instructions()

# Main game loop
while True:

    # get the range the secret number is between
    lowest = int_check("Low number: ")
    highest = int_check("High Number: ", lowest + 2)

    # Ask user for # of rounds then loop...
    rounds_played = 0

    # initialise counters
    rounds_won = 0
    rounds_lost = 0
    rounds = 0
    score = 0
    outcome = ""

    # set lists for game summary
    game_summary = []
    round_score = []

    # set the mode to regular
    mode = "regular"

    # Ask user for # of rounds, <enter> for indefinite mode
    mode_valid = "no"
    while mode_valid == "no":
        rounds = int_check("How many rounds?: ", 1, None, "xxx")
        if rounds == "":
            mode = "infinite"
            break
        elif rounds == "xxx":
            print("Please enter a integer higher than (or equal to) 1. ")
            continue
        else:
            break

    # Ask user for choice and check that it's valid
    # Start of gameplay loop
    end_game = "no"
    while end_game == "no":

        # Set Rounds Heading depending on the mode
        print()
        if mode == "infinite":
            heading = f"Continuous Mode: Round {rounds_played + 1}"
        else:
            heading = f"Round of {rounds_played + 1} of {rounds}"

        print(heading)

        # get the secret number
        secret_num = random.randint(lowest, highest)

        # calculate the number of guesses allowed
        guess_range = highest - lowest + 1
        max_raw = math.log2(guess_range)
        max_upped = math.ceil(max_raw)
        guesses_allowed = max_upped + 1
        if highest == lowest + 2:
            guesses_allowed -= 1
        print(f"Max Guesses: {guesses_allowed}")

        guesses_left = guesses_allowed

        # set list to prevent duplicates
        already_guessed = []

        while True:
            # compare numbers
            # get users guess
            guess = int_check("Guess a number: ", lowest, highest, "xxx")

            # End game if exit code is typed
            if guess == "xxx":
                end_game = "yes"
                break

            elif guess == "":
                print(f"Please enter a number between {lowest} and {highest}.")

            # checks that guess is not a duplicate
            elif guess in already_guessed:
                print(
                    f"You already guessed that number! Please try again. You *still* have {guesses_left} guesses left")
                continue

            elif guess != secret_num:
                guesses_left -= 1

                # Append the number guessed to avoid duplicates
                already_guessed.append(guess)

                # check if the guess is lower or higher than the secret number, then tell the user
                # if the number of guesses left is less than one, the user lost
                if guesses_left < 1:
                    statement_decorator("You ran out of guesses :(. Good luck next time!", "-")
                    # results for summary
                    rounds_lost += 1
                    outcome = "Round {}:\n You ran out og guesses".format(rounds_played + 1)
                    score = guesses_allowed + 1
                    break

                elif guess < secret_num:
                    statement_decorator("Too low, try a higher number. Guesses left: {}".format(guesses_left), "↑", )
                elif guess > secret_num:
                    statement_decorator("Too high, try a lower number. Guesses left: {}".format(guesses_left), "↓")

            # if the guess is the same as the secret number, the user wins
            elif guess == secret_num:
                if guesses_left == guesses_allowed:
                    # custom message if the got it in one
                    statement_decorator(f"Amazing! You got it in one!", "*")
                    score = 1
                else:
                    guesses_left -= 1
                    statement_decorator(f"Well done. You got it in {guesses_allowed - guesses_left}", "!")
                    score = guesses_allowed - guesses_left
                # results for summary
                rounds_won += 1
                outcome = "Round {}:\n You got it in {}".format(rounds_played + 1, score)
                break

        # If the exit code was entered, don't append the outcome. Otherwise, add the outcome to the list
        if guess != "xxx":
            game_summary.append(outcome)
            round_score.append(score)
            rounds_played += 1
            # if the number of rounds is more than rounds played or the mode is infinite, continue game
            if mode == "infinite" or rounds > rounds_played:
                continue
            # otherwise, end game
            else:
                break

    # if at least one round has been completed, ask the user if they want to see a summary of their game,
    if rounds_played != 0:
        print()
        see_summary = yes_no("Would you like to see the summary of your game? ")
        if see_summary == "yes":
            # Calculate game statistics (Best score, worst score average)
            percent_win = rounds_won / rounds_played * 100
            percent_lost = rounds_lost / rounds_played * 100
            best_score = min(round_score)
            worst_score = max(round_score)
            ave_score = (sum(round_score)) / len(round_score)

            # print game summary heading
            print("***** Game History *****")
            for outcome in game_summary:
                # Print the outcome of each round
                print(outcome)

            print()

            # displays game stats with % values to the nearest whole number
            print("Game Statistics", "*")
            print("Win: {}, ({:.0f}%)\nLoss: {}, "
                  "({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost))
            # displays the best, worst and average score
            print(f"Best Score: {best_score:.0f}\nWorst Score: {worst_score:.0f}\nAverage Score: {ave_score:.2f}")

    # Asks if the user wants to replay the game
    print()
    replay = yes_no("Would you like to play again?: ")

    # If yes, Replay game
    if replay == "yes":
        continue
    # Else, end program
    else:
        break

# Thanks the user for playing
print()
print("Thank you for playing!!")
