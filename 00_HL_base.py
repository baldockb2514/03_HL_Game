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
