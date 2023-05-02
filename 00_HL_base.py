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
    situation = ""

    # set the situation depending on what parameters were entered
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

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
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}.")
                    continue

            # checks if a number is higher than low if only lower bounds are specified
            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is higher than (or equal to) {low}")
                    continue

            return response

        # If input it not an integer, print error and ask question again
        except ValueError:
            print("Please enter a integer. ")
            continue


# Main routine goes here

# Game Title
print()
statement_decorator("Welcome to Higher or Lower", "*")

# Set up a loop to replay the game
replay_game = "yes"
while replay_game == "yes":

    # ask if the user would like to see the instructions
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

    # initialise counters
    rounds_won = 0
    rounds_lost = 0
    rounds = 0
    guess = 0
    score = 0
    result = ""

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
            print("Please enter a integer. ")
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
        print(f"Max Guesses: {guesses_allowed}")
        guesses_left = guesses_allowed

        # set list to prevent duplicates
        already_guessed = []

        while guesses_left >= 1:
            # compare numbers
            # get users guess
            guess = int_check("Guess a number: ", lowest, highest, "xxx")

            # End game if exit code is typed
            if guess == "xxx":
                score = -1
                outcome = ""
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
                if guess < secret_num:
                    statement_decorator("Too low, try a higher number. Guesses left: {}".format(guesses_left), "↑",)
                elif guess > secret_num:
                    statement_decorator("Too high, try a lower number. Guesses left: {}".format(guesses_left), "↓")

            # if the guess is the same as the secret number, the user wins
            elif guess == secret_num:
                if guesses_left == guesses_allowed:
                    # custom message if the got it in one
                    statement_decorator(f"Amazing! You got it in one!", "*")
                else:
                    statement_decorator(f"Well done. You got it in {len(already_guessed) + 1}", "!")
                # results for summary
                score = guesses_allowed - len(already_guessed) + 1
                rounds_won += 1
                result = "Win"
                break

        # if the number of guesses left is less than one, the user lost
        else:
            statement_decorator("You lost. Good luck next time!", "-")
            # results for summary
            rounds_lost += 1
            result = "Lost"
            score = 0

        outcome = "Round {}:\n Result: {}, Score: {}".format(rounds_played + 1, result, score)

        # If the exit code was entered, don't append the outcome. Otherwise, add the outcome to the list
        if guess != "xxx":
            game_summary.append(outcome)
        # If the score is more than zero, add it to the list
        if score >= 0:
            round_score.append(score)

        # If the exit code is typed, end game
        if guess == "xxx":
            break
        else:
            rounds_played += 1
            # if the number of rounds is more than rounds played or the mode is infinite, continue game
            if mode == "infinite" or rounds > rounds_played:
                continue
            # otherwise, end game
            else:
                break

    # Calculate game statistics (Best score, worst score average)
    percent_win = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    best_score = min(round_score)
    worst_score = max(round_score)
    ave_score = (sum(round_score)) / len(round_score)

    # print game summary heading
    print(f"Score list:\n {round_score}")
    print()
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
    print()

    # Asks if the user wants to replay the game
    print()
    replay = yes_no("Would you like to play again?: ")
    # If yes, Replay game
    if replay == "yes":
        continue
    else:
        break

# Thanks the user for playing
print()
print("Thank you for playing!!")
