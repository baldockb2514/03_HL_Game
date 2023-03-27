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
    statement_decorator("How to Play", "*", "sides")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Get the high and low numbers for the number range
def int_check(question, low=None, high=None):
    situation = ""

    # if low and high
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

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

